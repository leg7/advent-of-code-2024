import sys
from collections import defaultdict
from pprint import pprint


input = sys.stdin.read().strip().split()
rocks = defaultdict(int)
for r in input:
    rocks[int(r)] = 1

def split_number(rock):
    s = str(rock)
    l = len(s) // 2
    return list(divmod(rock, 10 ** l))

def f(rock):
    if rock == 0:
        return [1]
    elif len(str(rock)) % 2 == 0:
        return split_number(rock)
    else:
        return [rock * 2024]

for i in range(75):
    new_rocks = defaultdict(lambda: 0)
    for r in rocks:
        child_stones = f(r)
        for c in child_stones:
            new_rocks[c] += rocks[r]
    print(i)
    rocks = new_rocks

pprint(sum(rocks.values()))


