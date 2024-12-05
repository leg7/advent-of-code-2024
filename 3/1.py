import fileinput
import re

txt = ""
for line in fileinput.input():
    txt += line

instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", txt)
print(len(instructions))
instructions = [re.sub(r"mul\(|\)", "", i) for i in instructions]
args = [i.split(',') for i in instructions]
args = [list(map(int, a)) for a in args]
results = [ a[0] * a[1] for a in args]
r = sum(results)

print(r)
