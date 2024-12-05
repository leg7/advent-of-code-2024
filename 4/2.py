import fileinput

txt = [ ]
for line in fileinput.input():
    txt.append(line.strip())

txt_len = len(txt)
line_len = len(txt[0])
num_matches = 0

for l in range(1, txt_len - 1):
    for c in range(1, line_len - 1):
        if txt[l][c] == 'A':
            left_diagonal = (txt[l-1][c-1] == 'S' and txt[l+1][c+1] == 'M')
            left_diagonal = left_diagonal or (txt[l-1][c-1] == 'M' and txt[l+1][c+1] == 'S')

            right_diagonal = (txt[l-1][c+1] == 'S' and txt[l+1][c-1] == 'M')
            right_diagonal = right_diagonal or (txt[l-1][c+1] == 'M' and txt[l+1][c-1] == 'S')

            if left_diagonal and right_diagonal:
                num_matches += 1

print(num_matches)
