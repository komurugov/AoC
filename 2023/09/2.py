import sys

summ = 0

for line in sys.stdin:
    seq = list(map(int, line.split()))
    ends = [seq[0]]
    while True:
        prev = seq
        seq = []
        end = True
        for i in range(1, len(prev)):
            dif = prev[i] - prev[i - 1]
            seq.append(dif)
            if dif != 0:
                end = False
        if end:
            break
        ends.append(seq[0])
    x = 0
    for i in range(len(ends) - 1, -1, -1):
        x = ends[i] - x
    summ += x
    
print(summ)
    