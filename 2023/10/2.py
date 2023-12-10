import sys

rules = {
'|': ([[0, -1], [0, 1]], ['|', '|']),
'-': ([[-1, 0], [1, 0]], ['-', '-']),
'L': ([[0, -1], [1, 0]], ['|', '-']),
'J': ([[-1, 0], [0, -1]], ['-', '|']),
'7': ([[-1, 0], [0, 1]],  ['-', '|']),
'F': ([[0, 1], [1, 0]],  ['|', '-'])
}

def tr(x):
    return 2 * x + 1

N = 140
NN = tr(N)

field = []
for i in range(NN):
    field.append([' '] * NN)

i = 0
for line in sys.stdin:
    for j in range(len(line) - 1):
        field[tr(i)][tr(j)] = line[j]
    i += 1

pos = [tr(111) - 1, tr(107)]   
src = [-1, 0]
nxt = '-'
cnt = 0

#for line in field:
#    print("".join(line))
    
while True:
    ch = field[pos[1]][pos[0]]
    field[pos[1]][pos[0]] = '#' 
    if ch != ' ':
        cnt += 1
    if ch == 'S':
        break
    if ch == ' ':
        ch = nxt
    rule = rules[ch]
#    print(ch)
#    print(rule)
    ind = 1 - rule[0].index(src)
    dst = rule[0][ind]
    nxt = rule[1][ind]
    pos[0] += dst[0]
    pos[1] += dst[1]
    src[0] = -dst[0]
    src[1] = -dst[1]
#    print(ind, dst, nxt, src)

field[0][0] = 'o'

outers = 0
procEnd = True

def proc(x, y):
    global outers
    global procEnd
    if not (x in range(NN) and y in range(NN)):
        return
    if field[y][x] != 'o' and field[y][x] != '#':
        if field[y][x] != ' ':
            outers += 1
        field[y][x] = 'o'
        procEnd = False


while True:
    procEnd = True
    for y in range(NN):
        for x in range(NN):
            if field[y][x] == 'o':
                proc(x - 1, y - 1)
                proc(x, y - 1)
                proc(x + 1, y - 1)
                proc(x + 1, y)
                proc(x + 1, y + 1)
                proc(x, y + 1)
                proc(x - 1, y + 1)
                proc(x - 1, y)
    if procEnd:
        break
    
print(N * N - cnt - outers)    
#exit()    
    
for line in field:
    print("".join(line))
    
# < 1095