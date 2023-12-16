import sys

grid = []

for line in sys.stdin:
    grid.append(line[:-1])
    
W = len(grid[0])
H = len(grid)
print(W, H)

up = (-1, 0)
down = (1, 0)
right = (0, 1)
left = (0, -1)

path = []
for i in range(H):
    row = []
    for j in range(W):
        row.append({up: False, down: False, left: False, right: False})
    path.append(row)
    
rules = {
'.': {up: [up], down: [down], right: [right], left: [left]},
'/': {up: [right], down: [left], right: [up], left: [down]},
'\\': {up: [left], down: [right], right: [down], left: [up]},
'|': {up: [up], down: [down], right: [up, down], left: [up, down]},
'-': {up: [left, right], down: [left, right], right: [right], left: [left]}
}    
    
    
def go(y, x, dr):
    while True:
        if not y in range(H) or not x in range(W):
            return
        nxt = rules[grid[y][x]][dr]
        if len(nxt) > 1:
            for nx in nxt:
                if not path[y][x][nx]:
                    path[y][x][nx] = True
        #            print(y, x, '->', y + nx[0], x + nx[1])
                    go(y + nx[0], x + nx[1], nx)
            return
        else:
            if not path[y][x][nxt[0]]:
                path[y][x][nxt[0]] = True
                y += nxt[0][0]
                x += nxt[0][1]
                dr = nxt[0]
            else:
                return
 
def calc():
    summ = 0
    for row in path:
        for cell in row:
            if cell[up] or cell[down] or cell[left] or cell[right]:
                summ += 1
    return summ

maxim = 0

for i in range(W):
    go(0, i, (1, 0))
    maxim = max(maxim, calc())
    go(H - 1, i, (-1, 0))
    maxim = max(maxim, calc())

for i in range(H):
    go(i, 0, (0, 1))
    maxim = max(maxim, calc())
    go(i, W - 1, (0, -1))
    maxim = max(maxim, calc())
    
print(maxim)

   
# < 11537          
            
    
    