import time
import math

with open("day6-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()
    lines = list(map(lambda x: x.split(), lines))

count = 0
cols = list(map(list, zip(*lines)))

for col in cols:
    if col[-1] == '+':
        count += sum(map(int, col[:-1]))
    else:
        count += math.prod(map(int, col[:-1]))

print(count)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")
