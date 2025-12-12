import time

with open("day7-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

beams = {lines[0].index('S')}
count = 0

for line in lines[1:]:
    for i in list(beams):
        if line[i] == '^':
            count += 1
            beams.remove(i)
            beams.update([i-1, i+1])

print(count)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")