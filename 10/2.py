from fileinput import input
from pprint import pprint
from collections import defaultdict

map = []
trailhead_coords = []
for l,line in enumerate(input()):
    line = line.strip()

    heights = [int(c) for c in line]
    map.append(heights)

    trailheads = [(l,c) for c,char in enumerate(line) if char == '0']
    trailhead_coords.append(trailheads)

map_len = len(map)
map_width = len(map[0])

trailhead_coords = [x for xs in trailhead_coords for x in xs]

def summits(coord):
    l, c = coord
    current_height = map[l][c]
    if current_height != 0:
        return 0

    summits = defaultdict(int)
    _valid_trails_rec(coord, summits)
    return summits

# north, north east, east, ...
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def _valid_trails_rec(coord, summits):
    l, c = coord
    current_height = map[l][c]
    if current_height == 9:
        summits[coord] += 1
        return

    next_height = current_height + 1
    valid = 0
    for (l_, c_) in directions:
        neighbor_coords = (l + l_, c + c_)
        out_of_bounds = neighbor_coords[0] < 0 or neighbor_coords[0] >= map_len
        out_of_bounds = out_of_bounds or neighbor_coords[1] < 0 or neighbor_coords[1] >= map_width
        if out_of_bounds:
            continue

        neighbor = map[neighbor_coords[0]][neighbor_coords[1]]
        if neighbor == next_height:
            _valid_trails_rec(neighbor_coords, summits)
        else:
            continue


total_trails = 0
for coord in trailhead_coords:
    l, c = coord
    sm = summits(coord)
    for k in sm:
        total_trails += sm[k]

print(total_trails)





