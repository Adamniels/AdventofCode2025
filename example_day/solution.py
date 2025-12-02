"""
Advent of Code 2025 - Day example
https://adventofcode.com/2025/day/example
"""

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    lines = data.split('\n')

    result = 0
    
    return result

######### Part 2 ######### ######### 
def part2(data):
    lines = data.split('\n')
    
    result = 0
    
    return result


if __name__ == "__main__":
    # Testa med exempel
    # Note: don't forget to read correct input day
    example = read_input("day00/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day00/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
