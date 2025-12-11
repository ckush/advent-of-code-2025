from collections import defaultdict
import copy
import time

def adjacent_rolls(grid, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and (i!=row or j!=col) and grid[i][j] == '@':
                count += 1
    
    return count


with open("day4-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()
    grid = []
    count = 0
    last_removed = 1
    for line in lines:
        line = line.strip()
        grid.append(list(line))

    # print("======== Starting grid is ...=========")
    # for row in grid:
    #     print(row)
    
    while last_removed > 0:
        grid_crossed = copy.deepcopy(grid)
        last_removed = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@' and adjacent_rolls(grid, row, col) < 4:
                    last_removed += 1
                    grid_crossed[row][col] = '.'

        # print(f"======== Updated grid is ...=========")
        # for row in grid_crossed:
        #     print(row)
        
        grid = grid_crossed
        count += last_removed

    print(f"Total removed - {count}")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")