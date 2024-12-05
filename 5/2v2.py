import fileinput
from collections import defaultdict
from functools import cmp_to_key

sum = 0
is_before = defaultdict(lambda: defaultdict(bool))
importing_rules = True

cmp = cmp_to_key(lambda x, y: -1 if is_before[x][y] else 1)

for line in fileinput.input():
    if line == "\n":
        importing_rules = False
        continue

    if importing_rules:
        num, before = line.strip().split('|')
        is_before[num][before] = True
    else:
        pages = line.strip().split(',')
        fixed_pages = sorted(pages, key=cmp)
        ordered = pages == fixed_pages # i.e there was nothing to fix

        if not ordered:
            middle_value = fixed_pages[len(pages) // 2]
            sum += int(middle_value)

print(sum)







