import fileinput
import functools
from collections import Counter

left = []
right = Counter()

for line in fileinput.input(encoding="utf-8"):
    l, r = map(int, line.strip().split())
    left.append(l)
    right[r] += 1

print(sum(map(lambda x: x * right[x], left)))
