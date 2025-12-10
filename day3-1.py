with open("day3-1-input.txt") as f:
    lines = f.readlines()
    joltages = []
    for line in lines:
        max_joltage = max([digit+max(line[i+1:]) for i, digit in enumerate(line.strip()[:-1])])
        joltages.append(int(max_joltage))
    print(sum(joltages))