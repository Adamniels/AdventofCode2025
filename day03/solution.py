"""
Advent of Code 2025 - Day 3
https://adventofcode.com/2025/day/03
"""

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    lines = data.split('\n')
    result = 0


    for line in lines:
        max_nr = find_max_nr_in_bank(line)
        result += max_nr
    
    return result

def find_max_nr_in_bank(line:str) -> int:
    ental = int(line[-1])
    tiotal = int(line[-2])
    for i in range(len(line) - 3, -1, -1):
        c = int(line[i])
        if c >= tiotal:
            prev_tiotal = tiotal
            tiotal = c
            if prev_tiotal > ental:
                ental = prev_tiotal

    return int(str(tiotal) + str(ental))


######### Part 2 ######### ######### 
def part2(data):
    lines = data.split('\n')
    
    result = 0

    for line in lines:
        max_nr = find_max_nr_in_bank_part2(line)
        result += max_nr
    
    return result

def find_max_nr_in_bank_part2(line:str) -> int:
    tot = ""
    n = len(line)
    L = 12
    antal_kvar = L
    i = 0
    while antal_kvar > 0:
        k = n - (antal_kvar-1)
        i, nr = find_max_in_intervall(line, i, k)
        antal_kvar -= 1
        tot += str(nr)
        i += 1

    return int(tot)

def find_max_in_intervall(line:str, index:int, k:int):
    i = index
    max_nr = 0
    max_index = index

    while i < k:
        nr = int(line[i])
        if nr > max_nr:
            max_nr = nr
            max_index = i
        i += 1


    return max_index, max_nr

if __name__ == "__main__":
    # Testa med exempel
    example = read_input("day03/example.txt")
    # print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")

    print()

    # Kör med riktig input
    data = read_input("day03/input.txt")
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
