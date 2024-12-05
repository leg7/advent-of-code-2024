import fileinput
import functools
import operator

safeReports = 0
for line in fileinput.input(encoding = "utf-8"):
    levels = line.strip().split()
    levels = list(map(int, levels))
    print(levels)

    pairs = list(zip(levels, levels[1:]))
    print(pairs)

    diffs = list(map(lambda pair: pair[0] - pair[1], pairs))
    print(diffs)

    increasing = all(x > 0 for x in diffs)
    decreasing = all(x < 0 for x in diffs)
    print(increasing)
    print(decreasing)

    if (increasing or decreasing) and all(abs(x) >= 1 and abs(x) <= 3 for x in diffs):
        print('ok')
        safeReports += 1

    print('\n')

print(safeReports)
