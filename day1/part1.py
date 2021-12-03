#!/usr/bin/python3.9
from typing import List


def load_input(filepath: str) -> List[int]:
    results = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            results.append(int(line.strip()))
    return results


if __name__ == "__main__":
    measurements = load_input("day1/data.txt")

    counter = 0

    for idx, measurement in enumerate(measurements[1::], start=0):
        previous = measurements[idx]
        if measurement > previous:
            counter += 1

    print(counter)
