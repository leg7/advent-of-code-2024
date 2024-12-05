import fileinput
import functools
import operator

def safe(levels):
    pairs = list(zip(levels, levels[1:]))

    diffs = list(map(lambda pair: pair[0] - pair[1], pairs))

    increasing = [x < 0 for x in diffs]
    decreasing = [x > 0 for x in diffs]
    diffsValid = [1 <= abs(x) <= 3 for x in diffs]

    allGood = (all(increasing) or all(decreasing)) and all(diffsValid)
    return allGood

safeReports = 0
for line in fileinput.input(encoding = "utf-8"):
    levels = line.strip().split()
    levels = list(map(int, levels))

    if safe(levels):
        safeReports += 1
    else:
        for i in range(len(levels)):
            if (safe([x for j, x in enumerate(levels) if j != i])):
                safeReports += 1
                break



print(safeReports)
