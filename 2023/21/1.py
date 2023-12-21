import sys

garden = []
x = -1
for line in sys.stdin:
    if x == -1:
        x = line.find('S')
        if x != -1:
            y = len(garden)
    garden.append([ch for ch in line[:-1]])

H = len(garden)
W = len(garden[0])    
print(H, W)

nxtPlots = [(y, x)]

def paint(y, x):
    if y in range(H) and x in range(W) and garden[y][x] != '#':
        nxtPlots.append((y, x))

for steps in range(64):
    print(steps, len(nxtPlots))
    plots = nxtPlots
    nxtPlots = []
    for plot in plots:
        paint(plot[0] - 1, plot[1])
        paint(plot[0] + 1, plot[1])
        paint(plot[0], plot[1] - 1)
        paint(plot[0], plot[1] + 1)
        
print(len(nxtPlots))