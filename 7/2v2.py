from fileinput import input
from pprint import pprint
import functools

eqs = []
for line in input():
    line = line.strip().split(':')
    line[1] = line[1].split()
    line[1] = [int(x) for x in line[1]]
    line[0] = int(line[0])
    target, values = line
    eqs.append((target, values))

# You can probably optimise by pruning numbers that exceed the target from each iteration
def possibilities(values):
    if (len(values) == 1):
        return [values[0]]

    res = possibilities(values[1:])
    plus = [values[0] + x for x in res]
    mul = [values[0] * x for x in res]
    concat = [int(str(x) + str(values[0])) for x in res]
    return plus + mul + concat

answer = 0
for eq in eqs:
    target, values = eq
    values.reverse()
    if target in possibilities(values):
        answer += target

# print(answer)





