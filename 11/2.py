from fileinput import input

for line in input():
    rocks = line.strip().split()
    break

rocks = [int(r) for r in rocks]

def split_number(rock):
    s = str(rock)
    l = len(s) // 2
    return list(divmod(rock, 10 ** l))

# If rock is 0 it will cycle
def f(rock, iterations_left):
    if rock == 0:
        return ('L', 3 + 2 * (iterations_left - 1))
    elif len(str(rock)) % 2 == 0:
        return split_number(rock)

    else:
        return [rock * 2024]

def flatten(rocks):


for i in range(25):
    print(i)
    rocks = [ f(x) for x in rocks ]
    rocks = [x for xs in rocks for x in xs]

print(len(rocks))



