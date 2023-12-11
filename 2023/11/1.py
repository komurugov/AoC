import sys, math

row = 0
glxs = []
N = 140
cols = [0] * N

for line in sys.stdin:
    empty = True
    for col in range(len(line) - 1):
        if line[col] == '#':
            glxs.append([row, col])
            empty = False
            cols[col] += 1
    if empty:
        row += 1
    row += 1
    
for col in range(N - 1, -1, -1):
    if cols[col] == 0:
        for gal in glxs:
            if gal[1] > col:
                gal[1] += 1
                
summ = 0
for i in range(len(glxs)):
    for j in range(i + 1, len(glxs)):
        dst = math.abs(glxs[i][0] - glxs[j][0]) + math.abs(glxs[i][1] - glxs[j][1])
        summ += dst
    
    
print(summ)
    