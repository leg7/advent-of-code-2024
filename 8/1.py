from fileinput import input
from collections import defaultdict
from pprint import pprint

antennas = defaultdict(list)
map = []
for l,line in enumerate(input()):
    map.append(line.strip())
    for c,char in enumerate(line.strip()):
        if char != '.':
            antennas[char].append((c,l))

line_len = len(map[0])
map_len = len(map)

def add(tup_a, tup_b):
    return (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])

def in_bound(tup):
    return (tup[0] >= 0 and tup[0] < line_len) and (tup[1] >= 0 and tup[1] < map_len)

antinodes = defaultdict(lambda: defaultdict(bool))
for freq in antennas:
    freq_antennas = antennas[freq]
    pairs = [ (a,b) for a in freq_antennas for b in freq_antennas if a != b and a < b ]
    distances_1_2 = [ (x1 - x2, y1 - y2) for ((x1, y1), (x2, y2)) in pairs ]
    distances_2_1 = [ (x2 - x1, y2 - y1) for ((x1, y1), (x2, y2)) in pairs ]

    for i,(a,b) in enumerate(pairs):
        antinode_a = add(a, distances_1_2[i])
        antinode_b = add(b, distances_2_1[i])

        if in_bound(antinode_a):
            antinodes[freq][antinode_a] = True
        if in_bound(antinode_b):
            antinodes[freq][antinode_b] = True

pprint(antinodes)

all_antinodes = defaultdict(bool)
total = 0
for freq in antinodes:
    for an in antinodes[freq]:
        all_antinodes[an] = True

print(len(all_antinodes))
