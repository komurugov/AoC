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
    path.append([{up: False, down: False, left: False, right: False}] * W)
    
rules = {
'.': {up: [up], down: [down], right: [right], left: [left]},
'/': {up: [right], down: [left], right: [up], left: [down]},
'\\': {up: [left], down: [right], right: [down], left: [up]},
'|': {up: [up], down: [down], right: [up, down], left: [up, down]},
'-': {up: [left, right], down: [left, right], right: [right], left: [left]}
}    
    
    
def go(y, x, dr):
    if not y in range(H) or not x in range(W):
        return
    nxt = rules[grid[y][x]][dr]
    for nx in nxt:
        if not path[y][x][nx]:
            path[y][x][nx] = True
            go(y + nx[0], x + nx[1], nx)
 
go(0, 0, (0, 1))

summ = 0
for row in path:
    for cell in row:
        if cell[up] or cell[down] or cell[left] or cell[right]:
            summ += 1
            
print(summ)

# > 2750            
            
    
    