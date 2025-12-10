def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i and n // i != n:
                factors.append(n // i)
    return sorted(factors)

with open("day2-1-input.txt") as f:
    lines = f.readlines()
    ranges = lines[0].split(',')
    count = 0
    for prodrange in ranges:
        start, end = [int(i) for i in prodrange.split('-')]
        len_start, len_end = len(str(start)), len(str(end))
        already_found = set()
        for length in [i for i in range(len_start, len_end+1) if i>1]:
            for repeating_length in find_factors(length):
                repeating_int = int(str(start)[:repeating_length]) if length==len_start else 10**(repeating_length -1)
                candidate = int(str(repeating_int)*(length//repeating_length))
                print("=========", start, end, length, repeating_length, repeating_int, candidate, candidate >= start, len(str(candidate)), length, already_found)
                while candidate <= end and len(str(candidate)) == length:
                    if candidate >= start and candidate not in already_found:
                        print(candidate)
                        count += candidate
                        already_found.add(candidate)
                    repeating_int += 1
                    candidate = int(str(repeating_int)*(length//repeating_length))
            print("count is ", count)
    print(count)