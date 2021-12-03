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

    window_size = 3
    slide = window_size
    previous_sum = sum(measurements[0:slide])
    counter = 0

    for idx in range(len(measurements)):
        window = measurements[idx:slide]
        if len(window) == window_size:
            window_sum = sum(window)

            if window_sum > previous_sum:
                counter += 1

            previous_sum = window_sum

        slide += 1

    print(counter)
