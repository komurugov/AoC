import sys

rules = {
'|': [[0, -1], [0, 1]],
'-': [[-1, 0], [1, 0]],
'L': [[0, -1], [1, 0]],
'J': [[-1, 0], [0, -1]],
'7': [[-1, 0], [0, 1]],
'F': [[0, 1], [1, 0]]
}

field = []

for line in sys.stdin:
    field.append(line[:-1])
    
cnt = 1
pos = [111, 107]    
src = [-1, 0]
while True:
    ch = field[pos[1]][pos[0]]
    if ch == 'S':
        break
    rule = rules[ch]
    dst = rule[1 - rule.index(src)]
    cnt += 1
    pos[0] += dst[0]
    pos[1] += dst[1]
    src[0] = -dst[0]
    src[1] = -dst[1]
    
print(cnt / 2)