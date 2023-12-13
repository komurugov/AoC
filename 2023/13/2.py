import sys

summ = 0

rows = []
for line in sys.stdin:
    if len(line) < 3:
        H = len(rows)
        W = len(rows[0])
        print(H, W)

        for i in range(H - 1):
            neq = 0
            for j in range(min(i + 1, H - 1 - i)):
                for k in range(W):
                    #print(i, j, k)
                    if rows[i - j][k] != rows[i + 1 + j][k]:
                        neq += 1
                        if neq > 1:
                            break
                if neq > 1:
                    break
            if neq == 1:
                summ += 100 * (i + 1)
                break
                
        for i in range(W - 1):
            neq = 0
            for j in range(min(i + 1, W - 1 - i)):
                for k in range(H):
                    if rows[k][i - j] != rows[k][i + 1 + j]:
                        #print(i, j, k)
                        neq += 1
                        if neq > 1:
                            break
                if neq > 1:
                    break
            if neq == 1:
                summ += (i + 1)
                break
                
        rows = []
    else:
        rows.append(line[:-1])
        
print(summ)

# > 27159
# > 27259