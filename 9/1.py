import copy
from fileinput import input

for line in input():
    disk_map = line.strip()
    break

# print(disk_map)

empty = -1

uncompressed = []
id = 0
for i,c in enumerate(disk_map):
    if (i % 2 == 0):
        elem = [id] * int(c)
        id += 1
    else:
        elem = [empty] * int(c)
    uncompressed.append(elem)

uncompressed = [x for xs in uncompressed for x in xs]
print(uncompressed)

j = len(uncompressed) - 1
for i,c in enumerate(uncompressed):
    if j <= i:
        break

    if c == -1:
        while uncompressed[j] == empty:
            j -= 1
        uncompressed[i] = uncompressed[j]
        uncompressed[j] = empty
        j -= 1

print(uncompressed)

uncompressed = [int(x) for x in uncompressed if x != empty]
print(uncompressed)

checksum = 0
for i,x in enumerate(uncompressed):
    checksum += i * x

print(checksum)





