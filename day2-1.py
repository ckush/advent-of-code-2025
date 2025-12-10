with open("day2-1-input.txt") as f:
    lines = f.readlines()
    ranges = lines[0].split(',')
    count = 0
    for prodrange in ranges:
        start, end = [int(i) for i in prodrange.split('-')]
        len_start, len_end = len(str(start)), len(str(end))
        for length in [i for i in range(len_start, len_end+1) if i%2 == 0]:
            half_int = int(str(start)[:length//2]) if length==len_start else 10**(length//2 -1)
            candidate = int(str(half_int)*2)
            print("=========",start, end, length, half_int, candidate, candidate >= start)
            while candidate <= end and len(str(half_int)) == length//2:
                if candidate >= start:
                    print(candidate)
                    count += candidate
                half_int += 1
                candidate = int(str(half_int)*2)
    print(count)