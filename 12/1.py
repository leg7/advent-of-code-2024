import sys
from collections import defaultdict, deque
from dataclasses import dataclass

map = sys.stdin.read().split()
map_width = len(map[0])
map_height = len(map)

neighbor_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# regions = []
visited = defaultdict(bool)
price = 0
for l,line in enumerate(map):
    for c,_type in enumerate(line):
        # For each plant do a bfs to find the area and perimeter of it's region if not done already
        if visited[(l,c)]:
            continue
        visited[(l,c)] = True
        region_points = defaultdict(bool)
        region_points[(l,c)] = True
        perimeter = 0

        queue = deque()
        queue.appendleft((l,c))
        while len(queue) != 0:
            current_point = queue.pop()

            for offset in neighbor_offsets:
                neighbor = (current_point[0] + offset[0], current_point[1] + offset[1])

                out_of_bounds = neighbor[0] < 0 or neighbor[0] >= map_height or neighbor[1] < 0 or neighbor[1] >= map_width
                same_type = not out_of_bounds and map[neighbor[0]][neighbor[1]] == _type

                if out_of_bounds or not same_type:
                    perimeter += 1

                if not out_of_bounds and same_type and not visited[neighbor]:
                    visited[neighbor] = True
                    region_points[neighbor] = True
                    queue.appendleft(neighbor)

        area = len(region_points)
        region_price = area * perimeter
        price += region_price

        # regions.append(region_points) # not needed for part 1 it seems

print(price)


