import sys

summ = 0

rows = []
for line in sys.stdin:
    if len(line) < 3:
        H = len(rows)
        W = len(rows[0])
        print(H, W)

        for i in range(H - 1):
            eq = True
            for j in range(min(i + 1, H - 1 - i)):
                for k in range(W):
                    #print(i, j, k)
                    if rows[i - j][k] != rows[i + 1 + j][k]:
                        eq = False
                        break
                if not eq:
                    break
            if eq:
                summ += 100 * (i + 1)
                break
                
        for i in range(W - 1):
            eq = True
            for j in range(min(i + 1, W - 1 - i)):
                for k in range(H):
                    if rows[k][i - j] != rows[k][i + 1 + j]:
                        #print(i, j, k)
                        eq = False
                        break
                if not eq:
                    break
            if eq:
                summ += (i + 1)
                break
                
        rows = []
    else:
        rows.append(line[:-1])
        
print(summ)

# > 27159
# > 27259