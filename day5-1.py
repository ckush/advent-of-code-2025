import time

with open("day5-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

count = 0

# Read the file and separate input into ranges and ingredients
parts = "".join(lines).split("\n\n")
ranges = parts[0].strip().splitlines()
numbers = parts[1].strip().splitlines()
ranges = list(map(lambda x: tuple(map(int, x.split("-"))), ranges))
numbers = list(map(int, numbers))
ranges.sort()
numbers.sort()
# print(ranges)
# print(numbers)

for number in numbers:
    for start, end in ranges:
        if number in range(start, end+1):
            count += 1
            break


print(count)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")