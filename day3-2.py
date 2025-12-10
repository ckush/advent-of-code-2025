from collections import defaultdict
import time

def build_indices_map(line: str) -> dict:
    indices_map = defaultdict(list)
    for i, digit in enumerate(line):
        indices_map[digit].append(i)
    return indices_map

with open("day3-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()
    number_of_batteries = 12
    joltages = []
    for line in lines:
        line = line.strip()
        indices = build_indices_map(line)
        digits = []
        last_index = -1

        for i in range(number_of_batteries):
            next_digit = max(line[last_index+1:len(line)-(number_of_batteries-1-i)])
            last_index = min([j for j in indices[next_digit] if j > last_index])
            digits.append(next_digit)

        joltages.append(int(''.join(digits)))

    print(joltages)
    print(sum(joltages))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")