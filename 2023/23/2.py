import sys, copy

lines = []

for line in sys.stdin:
    lines.append(line[:-1])
    
H = len(lines)
W = len(lines[0])

print(H, W)

longest = 0

def Process(y, x, path, nxt):
    #print('proc', y, x)
    if x in range(W) and y in range(H) and not (y, x) in path and lines[y][x] != '#':
        #print('added')
        nxt.append((y, x))

def Recurse(pos, path):
    while True:
        if pos == (H - 1, W - 2):
            global longest
            longest = max(longest, len(path))
            #print(longest)
            return
        path.add(pos)
        nxt = []
        ch = lines[pos[0]][pos[1]]
        Process(pos[0] - 1, pos[1], path, nxt)
        Process(pos[0], pos[1] + 1, path, nxt)
        Process(pos[0] + 1, pos[1], path, nxt)
        Process(pos[0], pos[1] - 1, path, nxt)
        if len(nxt) == 0:
            return
        if len(nxt) == 1:
            pos = nxt[0]
            #print('nxt', pos)
        else:
            for n in nxt:
                #print('rec', n)
                Recurse(n, copy.copy(path))
            return    
    
Recurse((0, 1), set())

print(longest)