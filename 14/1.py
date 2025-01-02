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

for i in range(100):
    for r in range(len(robots)):
        x, y, vx, vy = robots[r]
        x = (x + vx)
        y = (y + vy)
        robots[r] = x, y, vx, vy

for i in range(100):
    for r in range(len(robots)):
        x, y, vx, vy = robots[r]
        x %= map_width
        y %= map_height
        robots[r] = x, y, vx, vy

top_left = [(x,y,vx,vy) for (x,y,vx,vy) in robots if x < map_width//2 and y < map_height//2]
top_right = [(x,y,vx,vy) for (x,y,vx,vy) in robots if x > map_width//2 and y < map_height//2]
bottom_right = [(x,y,vx,vy) for (x,y,vx,vy) in robots if x > map_width//2 and y > map_height//2]
bottom_left = [(x,y,vx,vy) for (x,y,vx,vy) in robots if x < map_width//2 and y > map_height//2]

print(len(top_left), len(top_right), len(bottom_left), len(bottom_right))
print(len(top_left) * len(top_right) * len(bottom_left) * len(bottom_right))

