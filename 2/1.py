import fileinput

reports = []
for line in fileinput.input(encoding = "utf-8"):
    levels = line.strip().split()
    levels = list(map(int, levels))
    reports.append(levels)

safeReports = 0
for r in reports:
    inc = r[0] > r[1]
    dec = r[0] < r[1]

    safe = True
    for i in range(len(r) - 1):
        stillInc = r[i] > r[i+1]
        stillDec = r[i] < r[i+1]
        diff = abs(r[i] - r[i+1])
        if not ((diff >= 1 and diff <= 3) and ((inc and stillInc) or (dec and stillDec))):
            safe = False
            break

    if safe:
        safeReports += 1

print(safeReports)
