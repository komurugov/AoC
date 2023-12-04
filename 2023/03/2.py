import sys

lines = []
gears = dict()

for line in sys.stdin:
    lines.append(line)

width = len(line) - 1
print(width)
hight = len(lines)
sum = 0

for row in range(0, hight):
    column = -1
    start = -1
    end = -1
    while True:
        column += 1
        if column >= width:
            if start != -1:
                end = column
        else:
            if lines[row][column].isdigit():
                if start == -1:
                    start = column
            else:
                if start != -1:
                    end = column
        if end != -1:
            num = int(lines[row][start:end])
            if row > 0:
                for x in range(start - 1, end + 1):
                    if x >= 0 and x < width:
                        ch = lines[row - 1][x]
                        if ch == '*':
                            if (row - 1, x) in gears:
                                gears[(row - 1, x)].append(num)
                            else:
                                gears[(row - 1, x)] = [num]
            if start > 0:
                ch = lines[row][start - 1]
                if ch == '*':
                    if (row, start - 1) in gears:
                        gears[(row, start - 1)].append(num)
                    else:
                        gears[(row, start - 1)] = [num]
            if end < width:
                ch = lines[row][end]
                if ch == '*':
                    if (row, end) in gears:
                        gears[(row, end)].append(num)
                    else:
                        gears[(row, end)] = [num]
            if row + 1 < hight:
                for x in range(start - 1, end + 1):
                    if x >= 0 and x < width:
                        ch = lines[row + 1][x]
                        if ch == '*':
                            if (row + 1, x) in gears:
                                gears[(row + 1, x)].append(num)
                            else:
                                gears[(row + 1, x)] = [num]

            start = -1
            end = -1

        if column >= width:
            break
            
for pos, adj in gears.items():
    if len(adj) == 2:
        sum += adj[0] * adj[1]
            
print(sum) # not 528105
print(','.isdigit())
            