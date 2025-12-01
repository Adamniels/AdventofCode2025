"""
Advent of Code 2025 - Day 1
https://adventofcode.com/2025/day/1
"""
from typing import Literal

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    lines = data.split('\n')

    result = 0

    current = 50 # Start position

    for line in lines:
        dir =line[0]
        nr = line[1:]

        current = rotate_part1(current, int(nr), dir)
        if current == 0:
            result += 1
    
    
    return result

def rotate_part1(current: int, steps: int, direction: Literal["L", "R"]) -> int:
    if direction == "L":
        return (current-steps)%100
    elif direction == "R":
        return (current+steps)%100

######### Part 2 ######### ######### 
def part2(data):
    lines = data.split('\n')
    
    result = 0

    current = 50 # Start position

    for line in lines:
        dir =line[0]
        nr = line[1:]
        prev = current
        current, hits = rotate_part2(current, int(nr), dir)
        result += hits
    
    
    return result

def rotate_part2(current: int, steps: int, direction: Literal["L", "R"]) -> tuple[int, int]:
    hits = 0

    for _ in range(steps):
        if direction == "L":
            current = (current - 1) % 100
        elif direction == "R":
            current = (current + 1) % 100
        else:
            raise ValueError(f"Not valid input rotate: {direction}")

        if current == 0:
            hits += 1

    return current, hits


if __name__ == "__main__":
    # Testa med exempel
    example = read_input("day01/example.txt")
    print(-3%100)
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day01/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
