#!/usr/bin/python3.9
from typing import List


def load_input(filepath: str) -> List[List[int]]:
    results = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = str(line.strip())
            results.append([int(d) for d in line])
    return results


if __name__ == "__main__":

    diagnostics = load_input("day3/data.txt")
    gamma = ""
    epsilon = ""
    for idx in range(len(diagnostics[0])):

        col = [d[idx] for d in diagnostics]
        if col.count(0) > col.count(1):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    consumption = int(gamma, 2) * int(epsilon, 2)
    print(f"Gamma -> Binary: {gamma} | Decimal: {int(gamma, 2)}")
    print(f"Epsilon -> Binary: {gamma} | Decimal: {int(epsilon, 2)}")
    print(f"Consumption -> {consumption}")
