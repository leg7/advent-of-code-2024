from fileinput import input
import re
from pprint import pprint

robots = []
for line in input():
    r = re.findall(r"[-0-9]*", line.strip())
    r = [int(x) for x in r if x != '']
    robots.append(r)

map_width = 101
map_height = 103

i = 0
min_safety_factor = 1034981770134982701
min_i = None
while i != 41850:
    for r in range(len(robots)):
        x, y, vx, vy = robots[r]
        x = (x + vx) % map_width
        y = (y + vy) % map_height
        robots[r] = x, y, vx, vy
    i += 1

    top_left = [x for (x,y,vx,vy) in robots if x < map_width//2 and y < map_height//2]
    top_right = [x for (x,y,vx,vy) in robots if x > map_width//2 and y < map_height//2]
    bottom_right = [x for (x,y,vx,vy) in robots if x > map_width//2 and y > map_height//2]
    bottom_left = [x for (x,y,vx,vy) in robots if x < map_width//2 and y > map_height//2]

    safety_factor = len(top_left) * len(top_right) * len(bottom_left) * len(bottom_right)
    if safety_factor < min_safety_factor:
        min_safety_factor = safety_factor
        min_i = i
        print(min_safety_factor, min_i)
        tmp = [(x,y) for (x,y,vx,vy) in robots]
        for h in range(map_height):
            for w in range(map_width):
                if (w,h) in tmp:
                    print('X', end='')
                else:
                    print('.', end='')
            print()
        print()


print(min_safety_factor, min_i)

