import fileinput
import operator
import functools
import re

txt = ""
for line in fileinput.input():
    txt += line

txt = txt.split(r"don't()")

txt = [x.split(r"do()") for x in txt]
txt = [txt[0]] + [x[1:] for x in txt[1:]]
txt = ["".join(x) for x in txt if x != []]
txt = "".join(txt)

txt = re.sub(r"don't\(\).*?$", "", txt)

instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", txt)
print(len(instructions))
instructions = [re.sub(r"mul\(|\)", "", i) for i in instructions]
args = [i.split(',') for i in instructions]
args = [list(map(int, a)) for a in args]
results = [ a[0] * a[1] for a in args]
r = sum(results)

print(r)
