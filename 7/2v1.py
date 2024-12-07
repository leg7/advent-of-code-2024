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


# I thought I had to make this left associative without reversing the input list
# to make concatenation work but I in the end I had the same problem where the
# concatenation would be done backwards.
# I didn't realise I would just swap the order of concatenation in the list
# comprehension to do it the the right order....
def possibilities(values):
    return go([values[0]], values[1:])

def go(acc, values):
    if (values == []):
        return acc

    plus = [values[0] + x for x in acc]
    mul = [values[0] * x for x in acc]
    concat = [int(str(x) + str(values[0])) for x in acc]
    return go(plus + mul + concat, values[1:])

answer = 0
for eq in eqs:
    target, values = eq
    p = possibilities(values)
    if target in p:
        answer += target


# print(answer)





