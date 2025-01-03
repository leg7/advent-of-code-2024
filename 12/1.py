import sys
from collections import defaultdict, deque
from dataclasses import dataclass

map = sys.stdin.read().split()
map_width = len(map[0])
map_height = len(map)

visited = set()
price = 0
for l,line in enumerate(map):
    for c,_type in enumerate(line):
        # For each plant do a BFS to find the area and perimeter of it's region if not done already

        already_visited = (l,c) in visited
        if already_visited:
            continue
        visited.add((l,c))

        region = set()
        region.add((l,c))
        perimeter = 0

        queue = deque()
        queue.appendleft((l,c))
        while len(queue) != 0:
            (i, j) = queue.pop()

            for neighbor in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                out_of_bounds = neighbor[0] < 0 or neighbor[0] >= map_height or neighbor[1] < 0 or neighbor[1] >= map_width
                same_type = not out_of_bounds and map[neighbor[0]][neighbor[1]] == _type

                if out_of_bounds or not same_type:
                    perimeter += 1

                already_visited = neighbor in visited
                if not out_of_bounds and same_type and not already_visited:
                    visited.add(neighbor)
                    region.add(neighbor)
                    queue.appendleft(neighbor)

        area = len(region)
        region_price = area * perimeter
        price += region_price

print(price)


