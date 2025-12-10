with open("day1-1-input.txt") as f:
    lines = f.readlines()
    pos = 50
    count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        pos = (pos+distance)%100 if direction == "R" else (pos-distance)%100
        if pos == 0:
            count += 1
    print(count)