import sys
from collections import defaultdict, deque
from dataclasses import dataclass

map = sys.stdin.read().split()
map_width = len(map[0])
map_height = len(map)


neighbor_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def out_of_bounds(lc):
    global map_height, map_width
    return lc[0] < 0 or lc[0] >= map_height or lc[1] < 0 or lc[1] >= map_width

# simple bfs
regions = []
visited = defaultdict(bool)
price = 0
for l,line in enumerate(map):
    for c,_type in enumerate(line):
        if visited[(l,c)]:
            continue

        queue = deque()
        queue.appendleft((l,c))
        visited[(l,c)] = True
        region_points = defaultdict(bool)
        region_points[(l,c)] = True
        perimeter = 0

        while len(queue) != 0:
            current_point = queue.pop()

            valid_neighbor_count = 0
            for offset in neighbor_offsets:
                neighbor = tuple_add(current_point, offset)

                if out_of_bounds(neighbor) or map[neighbor[0]][neighbor[1]] != _type:
                    perimeter += 1

                if not out_of_bounds(neighbor) and map[neighbor[0]][neighbor[1]] == _type and visited[neighbor] == False:
                    valid_neighbor_count += 1
                    visited[neighbor] = True
                    region_points[neighbor] = True
                    queue.appendleft(neighbor)

        area = len(region_points)
        region_price = area * perimeter
        price += region_price

        regions.append(region_points)



print(price)


