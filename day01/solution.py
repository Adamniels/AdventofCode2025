"""
Advent of Code 2025 - Day 1
https://adventofcode.com/2025/day/1
"""

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    lines = data.split('\n')
    
    # Din lösning här
    result = 0
    
    return result


def part2(data):
    lines = data.split('\n')
    
    # Din lösning här
    result = 0
    
    return result


if __name__ == "__main__":
    # Testa med exempel
    example = read_input("day01/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day01/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
