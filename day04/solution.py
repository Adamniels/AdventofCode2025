"""
Advent of Code 2025 - Day 4
https://adventofcode.com/2025/day/04
"""
##### HELPER #####

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()

def to_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

def print_grid(grid):
    for row in grid:
        print("".join(str(c) for c in row))

def part1(data):
    lines = data.split('\n')
    grid = to_grid(lines) 
    # print_grid(grid)

    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == "@" or grid[i][j] == "x"):
                adj = check_adj(grid, i, j)
                if adj < 4:
                    result += 1

    # print()
    # print_grid(grid)
    
    return result

def check_adj(grid, rad, col):
    adj =  0
    for i in range(-1, 2, 1):
        if rad+i < 0 or rad+i >= len(grid):
            continue

        for j in range(-1, 2, 1):
            if col+j < 0 or col+j >= len(grid[i]):
                continue

            if rad+i == rad and col+j == col:
                continue

            curr = grid[rad + i][col + j]
            if (curr == "@" or curr == "x"):
                adj += 1

    if adj < 4:
        grid[rad][col] = "x"
    return adj

######### Part 2 ######### ######### 
from collections import deque

# BFS lösning där jag bara går igenom alla som har under 4 och justerar dem som blivit påverkade
def part2(data):
    lines = data.split('\n')
    grid = to_grid(lines)
    rows = len(grid)
    cols = len(grid[0])

    # Listan med alla granne-offsets
    neighbors = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if not (dr == 0 and dc == 0)
    ]

    # 1. Räkna antal grannar
    adj_count = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            cnt = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    cnt += 1
            adj_count[r][c] = cnt

    # 2. Kö för alla med < 4 grannar
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@" and adj_count[r][c] < 4:
                q.append((r, c))

    removed = 0

    # 3. bfs variant 
    while q:
        r, c = q.popleft()

        if grid[r][c] != "@":
            continue

        if adj_count[r][c] < 4:
            grid[r][c] = "."
            removed += 1

            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    adj_count[nr][nc] -= 1
                    if adj_count[nr][nc] < 4:
                        q.append((nr, nc))

    return removed

if __name__ == "__main__":
    # Testa med exempel
    example = read_input("day04/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day04/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

