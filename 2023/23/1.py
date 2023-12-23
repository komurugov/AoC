import sys

lines = []

for line in sys.stdin:
    lines.append(line[:-1])
    
H = len(lines)
W = len(lines[0])

print(H, W)

longest = 0
nxt = []

def Process(x, y):
    if x in range(W) and y in range(H) and not (y, x) in path and lines[y][x] != '#':
        nxt.append((y, x))

def Recurse(pos, path):
    while True:
        if pos == (H - 1, W - 2)
            longest = max(longest, len(path))
            return
        path.add(pos)
        nxt = []
        ch = lines[pos[0]][pos[1]]
        if ch in ['.', '^']
            Process(pos[0] - 1, pos[1])
        if ch in ['.', '>']
            Process(pos[0], pos[1] + 1)
        if ch in ['.', 'v']
            Process(pos[0] + 1, pos[1])
        if ch in ['.', '^']
            Process(pos[0], pos[1] - 1)
        if len(nxt) == 1:
            pos = nxt[0]
        else:
            for n in nxt:
                Recurse(n, copy.copy(path))
    
Recurse((0, 1), set())

print(longest)