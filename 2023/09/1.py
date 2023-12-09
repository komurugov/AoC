import sys

summ = 0

for line in sys.stdin:
    seq = list(map(int, line.split()))
    ends = [seq[len(seq) - 1]]
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
        ends.append(dif)
    summ += sum(ends)
    
print(summ)
    