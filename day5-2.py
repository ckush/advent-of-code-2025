import time

with open("day5-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

count = 0

# Read the file and separate input into ranges and ingredients
parts = "".join(lines).split("\n\n")
ranges = parts[0].strip().splitlines()
ranges = list(map(lambda x: tuple(map(int, x.split("-"))), ranges))
ranges.sort()

curr_start, curr_end = ranges[0][0], ranges[0][1]

for i, (start, end) in enumerate(ranges):
    print(start,'-',end,',',i)
    if i == len(ranges)-1:              #it's the last range
        count += curr_end - curr_start + 1
    elif curr_end < ranges[i+1][0]:    #range doesn't overlap with next range
        count += curr_end - curr_start + 1
        curr_start, curr_end = ranges[i+1][0], ranges[i+1][1]   #reset to next range
    else:   #range overlaps with next range
        curr_end = max(curr_end, ranges[i+1][1])
    
print(count)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")