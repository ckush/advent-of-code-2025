with open("day1-1-input.txt") as f:
    lines = f.readlines()
    pos = 50
    count = 0
    count2 = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:]) if direction == "R" else -int(line[1:])
        full_turns = abs(distance) // 100
        distance = (abs(distance) % 100) * (1 if distance >= 0 else -1)
        touches_zero = 1 if pos and ((pos+distance) <= 0 or (pos+distance) >= 100) else 0
        count = count + full_turns + touches_zero
        print(pos, line.strip(), distance, full_turns, touches_zero)
        pos = (pos+distance)%100
        if pos == 0:
            count2 += 1
    print(count, count2)