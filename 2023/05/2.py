import sys

seeds = list(map(int, input().split()[1:]))
source = []
for i in range(len(seeds) // 2):
    source.append((seeds[2 * i], seeds[2 * i + 1]))
destination = []

def finalize(src, dst):
    for i in src:
        if i[1] > 0:
            dst.append((i[0], i[1]))

for line in sys.stdin:
    if line == '\n':
        finalize(source, destination)
        source = destination
        destination = []
    else:
        if line.find(':') == -1:
            rule = list(map(int, line.split()))
            x = rule[1]
            y = x + rule[2] - 1
            dlt = rule[0] - x
            for i in range(0, len(source)):
                a = source[i][0]
                b = a + source[i][1] - 1
                if y < a or x > b:
                    pass
                elif x <= a and y >= b:
                    destination.append((a + dlt, source[i][1]))
                    source[i] = (0, 0)
                elif x > a and y >= b:
                    destination.append((x + dlt, b - x + 1))
                    source[i] = (a, x - a)
                elif x <= a and y < b:
                    destination.append((a + dlt, y - a + 1))
                    source[i] = (y + 1, b - y)
                else:
                    destination.append((x + dlt, y - x + 1))
                    source[i] = (a, x - a)
                    source.append((y + 1, b - y))
                
finalize(source, destination)

mn = destination[0][0]
for dst in destination[1:]:
    if dst[0] < mn:
        mn = dst[0]

print(mn)
        
        
        
