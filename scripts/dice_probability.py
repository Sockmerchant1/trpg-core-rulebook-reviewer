#!/usr/bin/env python3
"""Exact probability helper for common tabletop RPG dice checks."""

from __future__ import annotations

import argparse
import itertools
import re
from collections import Counter
from fractions import Fraction


DICE_RE = re.compile(r"^(?:(\d*)d)?(\d+)$")


def parse_dice(expr: str) -> tuple[int, int]:
    match = DICE_RE.match(expr.strip().lower())
    if not match:
        raise ValueError(f"Unsupported dice expression: {expr}")
    count_text = match.group(1)
    count = int(count_text) if count_text else 1
    sides = int(match.group(2))
    if count < 1 or sides < 2:
        raise ValueError("Dice count must be at least 1 and sides at least 2")
    if count > 8 or sides > 1000:
        raise ValueError("Expression too large for exact enumeration")
    return count, sides


def distribution(expr: str) -> Counter[int]:
    count, sides = parse_dice(expr)
    totals: Counter[int] = Counter()
    for rolls in itertools.product(range(1, sides + 1), repeat=count):
        totals[sum(rolls)] += 1
    return totals


def expected_value(dist: Counter[int]) -> Fraction:
    total = sum(dist.values())
    return sum(Fraction(value * count, total) for value, count in dist.items())


def chance(dist: Counter[int], op: str, target: int) -> Fraction:
    total = sum(dist.values())
    if op == ">=":
        hits = sum(count for value, count in dist.items() if value >= target)
    elif op == ">":
        hits = sum(count for value, count in dist.items() if value > target)
    elif op == "<=":
        hits = sum(count for value, count in dist.items() if value <= target)
    elif op == "<":
        hits = sum(count for value, count in dist.items() if value < target)
    elif op in ("=", "=="):
        hits = sum(count for value, count in dist.items() if value == target)
    else:
        raise ValueError(f"Unsupported operator: {op}")
    return Fraction(hits, total)


def opposed(left_expr: str, right_expr: str) -> tuple[Fraction, Fraction, Fraction]:
    left = distribution(left_expr)
    right = distribution(right_expr)
    total = sum(left.values()) * sum(right.values())
    wins = ties = losses = 0
    for left_total, left_count in left.items():
        for right_total, right_count in right.items():
            outcomes = left_count * right_count
            if left_total > right_total:
                wins += outcomes
            elif left_total == right_total:
                ties += outcomes
            else:
                losses += outcomes
    return Fraction(wins, total), Fraction(ties, total), Fraction(losses, total)


def d20_advantage(target: int, mode: str) -> Fraction:
    dist: Counter[int] = Counter()
    for first in range(1, 21):
        for second in range(1, 21):
            if mode == "advantage":
                dist[max(first, second)] += 1
            elif mode == "disadvantage":
                dist[min(first, second)] += 1
            else:
                raise ValueError("Mode must be advantage or disadvantage")
    return chance(dist, ">=", target)


def fmt(value: Fraction) -> str:
    percent = float(value) * 100
    return f"{value.numerator}/{value.denominator} ({percent:.2f}%)"


def print_distribution(expr: str) -> None:
    dist = distribution(expr)
    print(f"Expression: {expr}")
    print(f"Expected value: {float(expected_value(dist)):.4f} ({expected_value(dist)})")
    print("Distribution:")
    total = sum(dist.values())
    for value in sorted(dist):
        probability = Fraction(dist[value], total)
        print(f"  {value}: {fmt(probability)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exact common dice probability helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    dist_parser = subparsers.add_parser("dist", help="Show distribution and expected value")
    dist_parser.add_argument("expr", help="Dice expression, such as 2d6 or d100")

    check_parser = subparsers.add_parser("check", help="Calculate target check probability")
    check_parser.add_argument("expr", help="Dice expression, such as 2d6 or d100")
    check_parser.add_argument("operator", choices=[">=", ">", "<=", "<", "=", "=="])
    check_parser.add_argument("target", type=int)

    opposed_parser = subparsers.add_parser("opposed", help="Compare two simple dice totals")
    opposed_parser.add_argument("left")
    opposed_parser.add_argument("right")

    adv_parser = subparsers.add_parser("d20", help="Calculate d20 advantage/disadvantage")
    adv_parser.add_argument("mode", choices=["normal", "advantage", "disadvantage"])
    adv_parser.add_argument("target", type=int, help="Target number for roll >= target")

    args = parser.parse_args()

    if args.command == "dist":
        print_distribution(args.expr)
    elif args.command == "check":
        dist = distribution(args.expr)
        probability = chance(dist, args.operator, args.target)
        print(f"{args.expr} {args.operator} {args.target}: {fmt(probability)}")
        print(f"Expected value: {float(expected_value(dist)):.4f} ({expected_value(dist)})")
    elif args.command == "opposed":
        wins, ties, losses = opposed(args.left, args.right)
        print(f"{args.left} vs {args.right}")
        print(f"Left wins: {fmt(wins)}")
        print(f"Ties: {fmt(ties)}")
        print(f"Left loses: {fmt(losses)}")
    elif args.command == "d20":
        if args.mode == "normal":
            probability = chance(distribution("1d20"), ">=", args.target)
        else:
            probability = d20_advantage(args.target, args.mode)
        print(f"d20 {args.mode} >= {args.target}: {fmt(probability)}")


if __name__ == "__main__":
    main()
