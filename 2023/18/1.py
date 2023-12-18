import sys

up = [-1, 0]
down = [1, 0]
right = [0, 1]
left = [0, -1]

dirs = {
'U': up,
'D': down,
'R': right,
'L': left
}

cmds = []
x = 0
y = 0
xmin = 0
xmax = 0
ymin = 0
ymax = 0
for line in sys.stdin:
    line = line.split()
    cmd = (dirs[line[0]], int(line[1]))
    cmds.append(cmd)
    x += cmd[0][1] * cmd[1]
    y += cmd[0][0] * cmd[1]
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)
    
H = ymax - ymin + 1 + 2
W = xmax - xmin + 1 + 2
x = -xmin + 1
y = -ymin + 1

field = []
for i in range(H):
    line = []
    for j in range(W):
        line.append(' ')
    field.append(line)
    
field[y][x] = '#'
for cmd in cmds:
    for i in range(cmd[1]):
        y += cmd[0][0]
        x += cmd[0][1]
        field[y][x] = '#'
        
cnt = 1
new = 1
field[0][0] = '.'

def paint(y, x):
    global new
    global cnt
    if y in range(H) and x in range(W):
        if field[y][x] == ' ':
            field[y][x] = '.'
            new += 1
            cnt += 1


while new > 0:
    new = 0
    for y in range(H):
        for x in range(W):
            if field[y][x] == '.':
                paint(y - 1, x - 1)
                paint(y - 1, x)
                paint(y - 1, x + 1)
                paint(y, x - 1)
                paint(y, x + 1)
                paint(y + 1, x - 1)
                paint(y + 1, x)
                paint(y + 1, x + 1)
                
print(H * W - cnt)
    