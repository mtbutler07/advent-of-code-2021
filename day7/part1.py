#!/usr/bin/python3.9
from typing import List

from statistics import median


def move(position: int, alignment: int):
    return abs(position - alignment)


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
    alignment = int(median(positions))

    for position in positions:
        fuel_spent += move(position, alignment)
    print(fuel_spent)
