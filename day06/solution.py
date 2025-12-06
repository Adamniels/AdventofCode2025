"""
Advent of Code 2025 - Day 6
https://adventofcode.com/2025/day/06
"""

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()

def to_grid(lines):
    grid = []
    for line in lines:
        grid.append(line.split())
    return grid

def print_grid(grid):
    for row in grid:
        print("".join(f"[{c}]" for c in row))

def eval_problem(values, sign):
    if sign == '+':
        return sum(values)
    elif sign == '*':
        res = 1
        for v in values:
            res *= v
        return res
    elif sign == '-':
        res = values[0]
        for v in values[1:]:
            res -= v
        return res
    elif sign == '/':
        res = values[0]
        for v in values[1:]:
            res //= v
        return res
    else:
        raise ValueError(f"Unknown operator: {sign}")

def part1(data):
    lines = data.split('\n')
    grid = to_grid(lines)
    numbers = grid[:-1]     
    signs = grid[-1]  

    result = 0

    for col in range(len(grid[0])):        
        sign = grid[-1][col]
        print(f"sign: {sign}")

        values = [int(numbers[row][col]) for row in range(len(numbers))]
        

        result += eval_problem(values, sign)

    return result

######### Part 2 ######### ######### 
def part2(data):
    lines = data.split('\n')
    total = 0
    numbers = lines[:-1]
    sign_str = lines[-1]

    
    curr_sign = 0
    next_sign = find_sign_index(sign_str, curr_sign + 1)
    continue_loop = True
    while continue_loop:
        if next_sign is None:
            next_sign = len(sign_str)+3
            continue_loop = False

        grid = create_grid(curr_sign, next_sign, numbers)

        cephal_values = get_cephal_values_from_grid(grid)

        total += eval_problem(cephal_values, sign_str[curr_sign])

        curr_sign = next_sign 
        next_sign = find_sign_index(sign_str, curr_sign+1)

    return total

def get_cephal_values_from_grid(grid):
    rows = len(grid)
    if rows == 0:
        return []

    cols = len(grid[0])
    values = []

    for c in range(cols - 1, -1, -1):
        digits = []
        for r in range(rows):
            ch = grid[r][c]
            if ch.isdigit():
                digits.append(ch)

        if not digits:
            continue

        value = int("".join(digits))
        values.append(value)

    return values


def find_sign_index(sign_str, start):
    SIGNS = set("+-*/")

    for i in range(start, len(sign_str)):
        if sign_str[i] in SIGNS:
            return i
    
    return None

def create_grid(start, end, numbers_arr):
    width = end - start
    grid = []

    for line in numbers_arr:
        segment = line[start:start + width]
        grid.append(list(segment))

    return grid


def print_char_grid(grid):
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    # Testa med exempel
    # Note: don't forget to read correct input day
    example = read_input("day06/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day06/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
