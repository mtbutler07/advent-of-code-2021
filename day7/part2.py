#!/usr/bin/python3.9
from typing import List

from statistics import mean


def move(position: int, alignment: int):
    distance = abs(position - alignment)
    expense = int(distance * (1 + distance) / 2)
    return expense


def load_input(filepath: str) -> List[List[int]]:
    results = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = str(line.strip())
            results.append(int(line))
    return results


if __name__ == "__main__":
    fuel_spent = 0
    positions = load_input("day7/data.txt")
    alignment = int(mean(positions))

    for position in positions:
        fuel_spent += move(position, alignment)
    print(fuel_spent)
