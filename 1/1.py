import fileinput
import functools

left = []
right = []

for line in fileinput.input(encoding="utf-8"):
    l, r = map(int, line.strip().split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

diff = [abs(l - r) for (l, r) in zip(left, right)]
print(sum(diff))
