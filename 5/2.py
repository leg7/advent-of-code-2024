import fileinput
from collections import defaultdict
import functools
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
        pages_len = len(pages)

        correct = True
        for i in range(0, pages_len - 1):
            for j in range(i + 1, pages_len):
                if not is_before[pages[i]][pages[j]]:
                    correct = False
                    break
            if not correct:
                break

        if not correct:
            fixed_pages = sorted(pages, key=cmp)
            middle_value = fixed_pages[pages_len // 2]
            sum += int(middle_value)

print(sum)







