import time
import math

# This data structure was created with chatgpt
class DSU:
    def __init__(s): s.p,s.sz={},{}
    def find(s,x):
        s.p.setdefault(x,x)
        if s.p[x]!=x: s.p[x]=s.find(s.p[x])
        return s.p[x]
    def union(s,a,b):
        ra,rb=s.find(a),s.find(b)
        if ra==rb: return
        if s.sz.get(ra,1)<s.sz.get(rb,1): ra,rb=rb,ra
        s.p[rb]=ra; s.sz[ra]=s.sz.get(ra,1)+s.sz.get(rb,1)
    def add_edge(s,a,b):
        s.p.setdefault(a,a); s.p.setdefault(b,b)
        s.sz.setdefault(a,1); s.sz.setdefault(b,1)
        s.union(a,b)
    def size(s,x): return s.sz.get(s.find(x),1)
    def components(s):
        from collections import defaultdict
        d=defaultdict(int)
        for v in s.p: d[s.find(v)]+=1
        return dict(d)

with open("day8-1-input.txt") as f:
    start_time = time.time()
    lines = f.readlines()

points = []
connections = 1000
connected = DSU()

for point in lines:
    xyz = [int(i) for i in point.strip().split(',')]
    points.append(xyz)

grid = [[0]*len(points) for _ in range(len(points))]

for i, point in enumerate(points):
    for j, point in enumerate(points):
        grid[i][j] = math.dist(points[i], points[j])


flat_grid = (tuple(sorted([i, j])) for i, row in enumerate(grid) for j, v in enumerate(row) if i!=j)
flat_grid = list(set(flat_grid))
flat_grid = sorted(flat_grid, key=lambda x: float('inf') if grid[x[0]][x[1]] == 0 else grid[x[0]][x[1]], reverse=True)

for _ in range(connections):
    i, j = flat_grid.pop()
    # print(f"Closest points are {points[i]} and {points[j]} with distance {grid[i][j]}")
    # print(f"connecting the points number {i} and {j}")
    connected.add_edge(i,j)
    


print(connected.components())
top_three = sorted(connected.components().values(), reverse = True)[0:3]
print(top_three)
print(math.prod(top_three))
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")
