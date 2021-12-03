#!/usr/bin/python3.9
from dataclasses import dataclass
from typing import List


@dataclass(repr=True)
class Submarine:
    position: int = 0
    depth: int = 0
    aim: int = 0

    def move(self, direction: str, units: int) -> None:
        if direction == "up":
            self.aim -= units

        elif direction == "down":
            self.aim += units

        elif direction == "forward":
            self.position += units
            self.depth += self.aim * units

    def get_location(self) -> int:
        return self.position * self.depth


def load_input(filepath: str) -> List[tuple]:
    results = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            direction, unit = line.split()
            record = (direction, int(unit))
            results.append(record)
    return results


instructions = load_input("day2/data.txt")
subby = Submarine()

for movement in instructions:
    subby.move(movement[0], movement[1])

print(subby)
print(subby.get_location())
