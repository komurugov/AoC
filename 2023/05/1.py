import sys

destination = list(map(int, input().split()[1:]))
source = destination
seedsCnt = len(destination)

def finalize(src, dst):
    for i in range(0, len(dst)):
        if dst[i] < 0:
            dst[i] = src[i]

for line in sys.stdin:
    if line == '\n':
        finalize(source, destination)
        source = destination
        destination = [-1] * seedsCnt
    else:
        if line.find(':') == -1:
            rule = list(map(int, line.split()))
            for seed in range(0, seedsCnt):
                if source[seed] in range(rule[1], rule[1] + rule[2]):
                    destination[seed] = rule[0] + (source[seed] - rule[1])
                
finalize(source, destination)

print(min(destination))
        
        
        
