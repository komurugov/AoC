import sys

summ = 0

rows = []
for line in sys.stdin:
    if line == '':
        H = len(rows)
        W = len(rows[0])

        for i in range(H - 1):
            eq = True
            for j in range(min(i + 1, H - i)):
                for k in range(W):
                    if rows[i - j, k] != rows[i + 1 + j, k]:
                        eq = False
                        break
                if not eq:
                    break
            if eq:
                summ + 100 * (i + 1)
                break
                
        for i in range(W - 1):
            eq = True
            for j in range(min(i + 1, W - i)):
                for k in range(H):
                    if rows[k, i - j] != rows[k, i + 1 + j]:
                        eq = False
                        break
                if not eq:
                    break
            if eq:
                summ + (i + 1)
                break
                
        rows = []
    else:
        rows.append(line)
        
print(summ)