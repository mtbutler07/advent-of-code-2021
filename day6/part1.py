#!/usr/bin/python3.9
from typing import List


def simulate(swarm: List) -> List[int]:
    results = []

    for fish in swarm:
        if fish == 0:
            results.append(6)
            results.append(8)
        else:
            results.append(fish - 1)
    return results


def load_input(filepath: str) -> List[List[int]]:
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip().split(",")
            results = [int(i) for i in line]
    return results


if __name__ == "__main__":
    current = load_input("day6/data.txt")
    for i in range(80):
        current = simulate(current)
    print(len(current))
