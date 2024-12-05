import fileinput

txt = [ ]
for line in fileinput.input():
    txt.append(line.strip())

txt_len = len(txt)
line_len = len(txt[0])
num_matches = 0

for l,line in enumerate(txt):
    for c in range(line_len):
        text_to_match = None
        if line[c] == 'X':
            text_to_match = "MAS"
        elif line[c] == 'S':
            text_to_match = "AMX"
        else:
            continue

        n = len(text_to_match)
        match = True
        if c + n < line_len:
            for i in range(n):
                offset = i + 1
                if line[c + offset] != text_to_match[i]:
                    match = False
                    break
            if match:
                print("horz: ", l, c)
                num_matches += 1

        match = True
        if l + n < txt_len:
            for i in range(n):
                offset = i + 1
                if txt[l + offset][c] != text_to_match[i]:
                    match = False
                    break
            if match:
                print("vert: ", l, c)
                num_matches += 1

        match = True
        if c + n < line_len and l + n < txt_len:
            for i in range(n):
                offset = i + 1
                if txt[l + offset][c + offset] != text_to_match[i]:
                    match = False
                    break
            if match:
                print("diag: ", l, c)
                num_matches += 1

        match = True
        if c + n < line_len and l - n >= 0:
            for i in range(n):
                offset = i + 1
                if txt[l - offset][c + offset] != text_to_match[i]:
                    match = False
                    break
            if match:
                print("diag: ", l, c)
                num_matches += 1

print(num_matches)













