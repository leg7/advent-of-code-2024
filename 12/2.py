import sys
from collections import defaultdict, deque
from dataclasses import dataclass

map = sys.stdin.read().split()
map_width = len(map[0])
map_height = len(map)

def out_of_bounds_(line_col):
    return not (line_col[0] in range(map_height) and line_col[1] in range(map_width))

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

        queue = deque()
        queue.appendleft((l,c))
        while len(queue) != 0:
            (i, j) = queue.pop()

            for neighbor in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                out_of_bounds = out_of_bounds_(neighbor)
                same_type = not out_of_bounds and map[neighbor[0]][neighbor[1]] == _type

                already_visited = neighbor in visited
                if not out_of_bounds and same_type and not already_visited:
                    visited.add(neighbor)
                    region.add(neighbor)
                    queue.appendleft(neighbor)

        # Types of corners to check (1 corner == 1 side)
        #
        # 4 Inside corners: bottom left, top right, ...
        # A. AA
        # AA .A
        #
        # 4 Outside corners: top right, bottom left, ...
        # *.*  ***
        # AA.  .AA
        # ***  *.*
        #
        # Algorithm idea: for every point in a region check
        # it's neighbors to see if they match one of the 8 corner type
        corners = 0
        for (i,j) in region:
            NW, W, SW, N, S, NE, E, SE = [
                (i+x, j+y) in region
                for x in range(-1, 2)
                for y in range(-1, 2)
                if x or y
            ]

            corners += sum([
                # inside corners
                N and W and not NW, # bottom right
                N and E and not NE, # bottom left
                S and W and not SW, # top right
                S and E and not SE, # top left
                # outside corners
                not N and not W,
                not N and not E,
                not S and not W,
                not S and not E
            ])

        area = len(region)
        region_price = area * corners
        price += region_price

print(price)



