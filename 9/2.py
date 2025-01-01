import sys
from collections import defaultdict
from pprint import pprint
from copy import deepcopy

# Import disk map
filename = sys.argv[1]
disk_map = open(filename, 'r').read()
disk_map = list(disk_map.strip())

# Decompress
file_id_and_block_size = list() # The key is the file ID and the contents is the block size
free_space_blocks = list()
file_id = 0
is_free_space = False
for size in disk_map:
    if is_free_space:
        free_space_blocks.append(int(size))
        is_free_space = False
    else:
        file_id_and_block_size.append((file_id, int(size)))
        file_id += 1
        is_free_space = True

# pprint(file_id_and_block_size)
# pprint(free_space_blocks)
# print()

moved_to_free_space = defaultdict(lambda: list()) # key is free space block index and content are the files moved to it

# Move files starting from the last one
i = len(file_id_and_block_size) - 1
while i >= 0:
    file = file_id_and_block_size[i]

    # This check is needed because we set the file to None if it was moved later in the loop
    if file == None:
        i -= 1
        continue
    else:
        (file_id, file_size) = file

    # Find a free space block that could fit the file
    moved = False
    j = 0
    while j < len(free_space_blocks) and not moved:
        moving_file_to_the_left = file_id > j
        if not moving_file_to_the_left:
            break

        free_size = free_space_blocks[j]

        if file_size <= free_size:
            # pprint(file_id_and_block_size)
            # pprint(moved_to_free_space)
            # pprint(free_space_blocks)
            # print()

            # move it and update the free space left
            moved_to_free_space[j].append(file)
            free_size_left = free_size - file_size
            free_space_blocks[j] = free_size_left
            file_id_and_block_size[i] = None

            # Update the preceding free space left where the file was originally
            free_space_blocks[i-1] += file_size

            # if there was proceeding free space concat it to the preceeding free space
            is_last_file = i == len(file_id_and_block_size) - 1 # e.g selected file is not the last one
            is_free_space_to_the_right = moved_to_free_space[i] == []
            if not is_last_file and is_free_space_to_the_right:
                proceding_free_size = free_space_blocks[i]
                free_space_blocks[i] = 0
                free_space_blocks[i-1] += proceding_free_size

            moved = True

        j += 1

    i -= 1

# pprint(file_id_and_block_size)
# pprint(moved_to_free_space)
# pprint(free_space_blocks)
# print()

new_disk_map = [file_id_and_block_size[0]]
k = 1
l = 0
while k < len(file_id_and_block_size):
    if l < len(free_space_blocks):
        for f in moved_to_free_space[l]:
            new_disk_map.append(f)

        free_size = free_space_blocks[l]
        if free_size > 0:
            new_disk_map.append(free_size)

        l += 1

    file = file_id_and_block_size[k]
    if file != None:
        new_disk_map.append(file)

    k += 1

# print(new_disk_map)

checksum = 0
pos = 0
for elem in new_disk_map:
    is_file = isinstance(elem, tuple)
    if is_file:
        (file_id, file_size) = elem
        for i in range(file_size):
            checksum += file_id * pos
            pos += 1
    else:
        pos += elem

print(checksum)
