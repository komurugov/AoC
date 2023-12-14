import sys

dish = []
objs = {}

for line in sys.stdin:
    dish.append(list(line[:-1]))
    
H = len(dish)
W = len(dish[0])
print(H, W)

cnt = 0
big = 1000000000
found = False
while cnt < big:

    for col in range(W):
        for row in range(H - 1):
            if dish[row][col] == '.':
                for i in range(row + 1, H):
                    ch = dish[i][col]
                    if ch == '#':
                        break
                    if ch == 'O':
                        dish[i][col] = '.'
                        dish[row][col] = 'O'
                        break

    for row in range(H):
        for col in range(W - 1):
            if dish[row][col] == '.':
                for i in range(col + 1, W):
                    ch = dish[row][i]
                    if ch == '#':
                        break
                    if ch == 'O':
                        dish[row][i] = '.'
                        dish[row][col] = 'O'
                        break

    for col in range(W):
        for row in range(H - 1, 0, -1):
            if dish[row][col] == '.':
                for i in range(row - 1, -1, -1):
                    ch = dish[i][col]
                    if ch == '#':
                        break
                    if ch == 'O':
                        dish[i][col] = '.'
                        dish[row][col] = 'O'
                        break

    for row in range(H):
        for col in range(W - 1, 0, -1):
            if dish[row][col] == '.':
                for i in range(col - 1, -1, -1):
                    ch = dish[row][i]
                    if ch == '#':
                        break
                    if ch == 'O':
                        dish[row][i] = '.'
                        dish[row][col] = 'O'
                        break
                        
    obj = str(dish)
    if obj in objs and not found:
        x = objs[obj]
        print(x, cnt)
        cnt += (big - cnt) // (cnt - x) * (cnt - x)
        print(cnt)
        found = True
    else:
        objs[obj] = cnt
    cnt += 1
        
#print(obj)

summ = 0
for col in range(W):
    for row in range(H):
        if dish[row][col] == 'O':
            summ += H - row
            
print(summ)

# < 93105