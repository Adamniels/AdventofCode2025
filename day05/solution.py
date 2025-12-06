"""
Advent of Code 2025 - Day 5
https://adventofcode.com/2025/day/05
"""

import bisect


def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def parse_database(data: str):
    blocks = data.strip().split("\n\n")
    range_lines = blocks[0].splitlines()
    id_lines = blocks[1].splitlines()

    ranges = []
    for line in range_lines:
        line = line.strip()
        start_str, end_str = line.split("-")
        ranges.append((int(start_str), int(end_str)))

    ids = []
    for line in id_lines:
        line = line.strip()
        ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges):
    """
    Sorterar och slår ihop överlappande och intilliggande intervall.
    """

    # sortera på start, sen end
    ranges.sort(key=lambda x: (x[0], x[1])) # sorterar först på start om dem är samma end, tror aldrig det är fallet men...
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        # Om överlapp eller direkt intill: slå ihop
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_fresh_ids(ranges, ids):
    starts = [s for (s, _) in ranges] # gör en lista av alla start värden, för att hitta rätt
    count = 0

    for x in ids:
        # hitta sista intervallet med start <= x via bibliotek bisect, lösnign för binärsökning i sorterad lista
        idx = bisect.bisect_right(starts, x) - 1
        if idx >= 0:
            start, end = ranges[idx]
            if start <= x <= end:
                count += 1

    return count


def part1(data):
    ranges, ids = parse_database(data)
    merged_ranges = merge_ranges(ranges)
    result = count_fresh_ids(merged_ranges, ids)
    return result


######### Part 2 ######### ######### 
def all_fresh_ids(ranges):
    count = 0
    for start, end in ranges:
        count += ((end+1) - start)

    return count

def part2(data):
    ranges, ids = parse_database(data)
    merged_ranges = merge_ranges(ranges)
    result = all_fresh_ids(merged_ranges)
    
    return result


if __name__ == "__main__":
    # Testa med exempel
    # Note: don't forget to read correct input day
    example = read_input("day05/example.txt")
    print(f"Example Part 1: {part1(example)}")
    print(f"Example Part 2: {part2(example)}")
    
    print()
    
    # Kör med riktig input
    data = read_input("day05/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
