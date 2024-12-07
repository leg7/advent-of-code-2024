# The rule to put down an obstacle are the following:
#
# if (the guard steps into a position he has already been)
#   if (putting an obstacle in front of him would make him go in the same
#       direction he was going in previously when he stepped here)
#           put obstacle down
# if (putting an obstacle in front of the guard at any moment will lead him
#     to walk into a postition he was in previously and in the same direction)
#           put obstacle down


from fileinput import input
from enum import Enum, auto
from collections import defaultdict, namedtuple
from pprint import pprint
import copy

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

PatrolPoint = namedtuple('PatrolPoint', ['l', 'c','d'])

map = []
state = None
for l,line in enumerate(input()):
    line = list(line.strip())
    map.append(line)

    try:
        c = line.index('^')
        starting_point = PatrolPoint(l, c, Direction.up)
    except ValueError:
        pass

line_len = len(map[0])
map_len = len(map)

def will_leave(patrol_point):
    match patrol_point.d:
        case Direction.up:    return patrol_point.l == 0
        case Direction.right: return patrol_point.c == line_len - 1
        case Direction.down:  return patrol_point.l == map_len - 1
        case Direction.left:  return patrol_point.c == 0

def meets_obstacle(patrol_point, map):
    match patrol_point.d:
        case Direction.up:    return map[patrol_point.l - 1][patrol_point.c] == '#'
        case Direction.right: return map[patrol_point.l][patrol_point.c + 1] == '#'
        case Direction.down:  return map[patrol_point.l + 1][patrol_point.c] == '#'
        case Direction.left:  return map[patrol_point.l][patrol_point.c - 1] == '#'

def step(patrol_point):
    l = patrol_point.l
    c = patrol_point.c
    match patrol_point.d: # Step
        case Direction.up:    l -= 1
        case Direction.right: c += 1
        case Direction.down:  l += 1
        case Direction.left:  c -= 1

    return PatrolPoint(l, c, patrol_point.d)

patrol_points = defaultdict(bool)
patrol_points[starting_point] = True
obstacles = defaultdict(bool)

current_point = starting_point
obstacles_met = defaultdict(bool)

# I give up I have an extra 30 obstacles and I have no idea why
while not will_leave(current_point):
    while not meets_obstacle(current_point, map):
        current_point = step(current_point)
        patrol_points[current_point] = True

        if will_leave(current_point):
            break
        if meets_obstacle(current_point, map):
            obs = step(current_point)
            obstacles_met[obs]
            break

        candidate = step(current_point)
        obs_met_c = copy.deepcopy(obstacles_met)
        obs_met_c[candidate] = True
        backup = map[candidate.l][candidate.c]
        map[candidate.l][candidate.c] = '#'

        point_if_obstacle = PatrolPoint(current_point.l, current_point.c, current_point.d.next())
        t = point_if_obstacle

        looped = False
        while not will_leave(t) and not looped:
            if meets_obstacle(t, map):
                obstacle = step(t)
                looped = obs_met_c[obstacle]
                if not looped:
                    t = PatrolPoint(t.l, t.c, t.d.next())
                    obs_met_c[obstacle] = True
            else:
                t = step(t)

        if looped:
            obstacles[(candidate.l, candidate.c)] = True

        map[candidate.l][candidate.c] = backup

    if will_leave(current_point):
        break

    if meets_obstacle(current_point, map):
        obs = step(current_point)
        obstacles_met[obs]

    # Change direction
    current_point = PatrolPoint(current_point.l, current_point.c, current_point.d.next())


# pprint(obstacles)
pprint(len(obstacles))
