import fileinput
from enum import Enum, auto
from pprint import pprint
import os
import time

# It would be more efficent to compress this but it's complicated
map = []
guard = None
for l,line in enumerate(fileinput.input()):
    line = list(line.strip())
    map.append(line)

    try:
        i = line.index('^')
        guard = (l, i)
    except ValueError:
        pass

red = "\033[31m"
green = "\033[32m"
grey = "\033[90m"
reset = "\033[0m"
def colored(char):
    match char:
        case 'X': return red + char + reset
        case '#': return green + char + reset
        case '.': return grey + char + reset
        case _: return char

def print_map():
    os.system('clear')

    for line in map:
        line = [colored(x) for x in line]
        print(''.join(line))
    time.sleep(0.05)

class Direction(Enum):
    up = auto()
    right = auto()
    down = auto()
    left = auto()

    def next(self):
        match self:
            case Direction.up: return Direction.right
            case Direction.right: return Direction.down
            case Direction.down: return Direction.left
            case Direction.left: return Direction.up

line_len = len(map[0])
map_len = len(map)
direction = Direction.up
l, c = guard
guard_leaves = False

# Mark starting pos
map[l][c] = 'X'
print_map()

# Patrol
while not guard_leaves:
    path_blocked = None
    match direction:
        case Direction.up:    path_blocked = map[l - 1][c] == '#'
        case Direction.right: path_blocked = map[l][c + 1] == '#'
        case Direction.down:  path_blocked = map[l + 1][c] == '#'
        case Direction.left:  path_blocked = map[l][c - 1] == '#'

    while not path_blocked:
        match direction: # Step
            case Direction.up:    l -= 1
            case Direction.right: c += 1
            case Direction.down:  l += 1
            case Direction.left:  c -= 1
        map[l][c] = 'X'
        print_map()

        match direction:
            case Direction.up:    guard_leaves = l == 0
            case Direction.right: guard_leaves = c == line_len
            case Direction.down:  guard_leaves = l == map_len - 1
            case Direction.left:  guard_leaves = c == 0
        if guard_leaves:
            break

        match direction:
            case Direction.up:    path_blocked = map[l - 1][c] == '#'
            case Direction.right: path_blocked = map[l][c + 1] == '#'
            case Direction.down:  path_blocked = map[l + 1][c] == '#'
            case Direction.left:  path_blocked = map[l][c - 1] == '#'

    direction = direction.next()


res = sum([x.count('X') for x in map])
print(res)






