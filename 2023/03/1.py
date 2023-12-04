import sys

lines = []

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
            part = False
            if row > 0:
                for x in range(start - 1, end + 1):
                    if x >= 0 and x < width:
                        ch = lines[row - 1][x]
                        if not ch.isdigit() and ch != '.':
                            part = True
            if start > 0:
                ch = lines[row][start - 1]
                if not ch.isdigit() and ch != '.':
                    part = True
            if end < width:
                ch = lines[row][end]
                if not ch.isdigit() and ch != '.':
                    part = True
            if row + 1 < hight:
                for x in range(start - 1, end + 1):
                    if x >= 0 and x < width:
                        ch = lines[row + 1][x]
                        if not ch.isdigit() and ch != '.':
                            part = True
            if part:
                num = int(lines[row][start:end])
                print(num)
                sum += num
            start = -1
            end = -1

        if column >= width:
            break
            
print(sum) # not 528105
print(','.isdigit())
            