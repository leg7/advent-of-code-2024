import copy
from fileinput import input
from collections import defaultdict

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
        uncompressed.append(elem)
    elif c != '0':
        elem = [empty] * int(c)
        uncompressed.append(elem)

i = len(uncompressed) - 1
swapped = defaultdict(bool)
while i >= 0:
    if uncompressed[i][0] != empty:
        k = 0
        while k < i:
            while uncompressed[k][0] != empty and k < i:
                k += 1

            if (uncompressed[i] == uncompressed[k]):
                break

            if len(uncompressed[k]) == len(uncompressed[i]) and not swapped[k]:
                # print("==", uncompressed[k], uncompressed[i])
                # print(uncompressed)
                uncompressed[k] = uncompressed[i]
                uncompressed[i] = [empty] * len(uncompressed[i])
                swapped[k] = True
                break
            elif len(uncompressed[k]) > len(uncompressed[i]) and not swapped[k]:
                # print('>', uncompressed[k], uncompressed[i])
                # print(uncompressed)
                diff = len(uncompressed[k]) - len(uncompressed[i])
                space_left = [empty] * diff
                space_used = [empty] * len(uncompressed[i])
                uncompressed[k] = uncompressed[i]
                uncompressed.pop(i)
                uncompressed.insert(k+1, space_left)
                uncompressed.insert(i+1, space_used)
                swapped[k] = True
                break
            else:
                # print('<', uncompressed[k], uncompressed[i])
                k += 1
    i -= 1
    # print()

# print(uncompressed)
# print()

uncompressed = [x for xs in uncompressed for x in xs]
# print(uncompressed)
# print()

uncompressed = list(map(lambda x: 0 if x == -1 else x, uncompressed))
print(uncompressed)
print()

checksum = 0
for i,x in enumerate(uncompressed):
    checksum += i * x

print(checksum)





