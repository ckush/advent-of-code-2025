import time
import math
# import itertools

def split_on_indices(line, indices):
    return [line[a:b] for a, b in zip([0] + list(map(lambda x: x+1, indices)), indices + [len(line)])]

with open("day6-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

indices = []        #indices to split columns
count = 0

# break the columns vertically wherever each row has a space
for i, val in enumerate(lines[0]):
    if all(row[i] == ' ' for row in lines):
        indices.append(i)

lines = [split_on_indices(line.rstrip("\n"), indices) for line in lines]

cols = list(map(list, zip(*lines)))

for col in cols:
    # for each col we turn the strings into columns
    # ['64 ','23 ','314'] becomes [('6', '2', '3'), ('4', '3', '1'), ('', '', '4')]
    if '+' in col[-1]:
        vertical_nums = list(zip(*col[:-1]))
        # join each number and add
        count += sum([int(''.join(i)) for i in vertical_nums])
    else:
        # right justify each line
        rjusted_nums = [s.rjust(max(map(len, col))) for s in col]
        vertical_nums = list(zip(*rjusted_nums[:-1]))
        count += math.prod([int(''.join(i)) for i in vertical_nums])

print(count)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")
