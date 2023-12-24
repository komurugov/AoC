import sys

paths = []

for line in sys.stdin:
    line = line.split('@')
    x1, y1, z1 = list(map(int, line[0].split(',')))
    vx, vy, vz = list(map(int, line[1].split(',')))
    if vx == 0:
        print('oops')
    a = vy / vx
    b = y1 - a * x1
    paths.append([a, b])
    
P = len(paths)    
cnt = 0
low = 7 #200000000000000
high = 27 #400000000000000
    
for p1 in range(P - 1):
    print(p1)
    for p2 in range(p1 + 1, P):
        #print(':', p2, paths[p1], paths[p2])
        div = paths[p1][0] - paths[p2][0]
        if div != 0:
            x = (paths[p2][1] - paths[p1][1]) / div
            if x >= low and x <= high:
                y = paths[p1][0] * x + paths[p1][1]
                if y >= low and y <= high:
                    print(p1, p2, x, y)
                    cnt += 1
                    
print(cnt)

# < 30256