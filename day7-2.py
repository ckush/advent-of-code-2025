import time

with open("day7-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

beams = {lines[0].index('S'): 1}   # format - beam_position: weight
count = 0

for line in lines[1:]:
    for i, weight in list(beams.items()):
        if line[i] == '^':
            count += 1
            beams.pop(i)
            beams[i-1] = beams.get(i-1, 0) + weight
            beams[i+1] = beams.get(i+1, 0) + weight
print(sum(beams.values()))
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")