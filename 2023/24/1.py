import sys

paths = []

for line in sys.stdin:
    line = line.split('@')
    x1, y1, z1 = line[0].split(',')
    vx, vy, vz = line[1].split(',')
    if vx == 0:
        print('oops')
    a = vy / vx
    b = y1 - a * x1
    paths.append([a, b])
    
P = len(paths)    
cnt = 0
limits = range(2E14, 4E14 + 1)
    
for p1 in range(P - 1):
    for p2 in range(p1 + 1, P):
        div = paths[p1][0] - paths[p2][0]
        if div != 0:
            x = (paths[p2][1] - paths[p1][1]) / div
            if x in limits:
                y = paths[p1][0] * x + paths[p1][1]
                if y in limits:
                    cnt += 1
                    
print(cnt)