#!/usr/bin/python3.9


def simulate(swarm: dict):
    results = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for i in range(8, 0, -1):
        results[i - 1] = swarm[i]

    results[6] += swarm[0]
    results[8] = swarm[0]
    return results


def load_input(filepath: str):

    results = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip().split(",")
            inputs = [int(i) for i in line]

    for i in inputs:
        results[i] += 1
    return results


if __name__ == "__main__":
    current = load_input("day6/data.txt")
    for i in range(256):
        current = simulate(current)
    print(sum(current.values()))
