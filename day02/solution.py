"""
Advent of Code 2025 - Day 2
https://adventofcode.com/2025/day/2
"""

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    ranges = data.split(',')
    result = 0
    for _range in ranges:
        result += invalid_ids(_range)
    
    return result

def invalid_ids(_range:str) -> int:
    range_split = _range.split('-')

    sum_invalid_ids = 0
    start = int(range_split[0])
    end = int(range_split[1])

    for i in range (start, end+1):
        if invalid_nr(i):
            sum_invalid_ids += i

    return sum_invalid_ids

def invalid_nr(nr:int) -> bool:
    string_nr = str(nr)
    if len(string_nr) % 2 == 1:
        return False
    
    middle = len(string_nr)//2
    first = string_nr[:middle]
    second = string_nr[middle:]

    return first == second



######### Part 2 ######### ######### 
def part2(data):
    ranges = data.split(',')

    result = 0
    for _range in ranges:
        result += invalid_ids_part2(_range)
    
    return result

def invalid_ids_part2(_range:str) -> int:
    range_split = _range.split('-')

    sum_invalid_ids = 0
    start = int(range_split[0])
    end = int(range_split[1])

    for i in range (start, end+1):
        if invalid_nr_part2(i):
            sum_invalid_ids += i

    return sum_invalid_ids

def invalid_nr_part2(nr:int) -> bool:
    s = str(nr)
    length = len(s)

    # Prova alla möjliga längder på delmönstret
    for size in range(1, length // 2 + 1):

        if length % size != 0:
            # total len must fit fully a number of times
            continue

        pattern = s[:size]

        if pattern * (length // size) == s:
            # a str with the same len as nr but with a repeating invalid nr that we are trying
            return True

    return False

if __name__ == "__main__":
    # Testa med exempel
    example = read_input("day02/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
     
    print()
    
    # Kör med riktig input
    data = read_input("day02/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
