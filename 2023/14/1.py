import sys

dish = []

for line in sys.stdin:
    dish.append(list(line[:-1]))
    
H = len(dish)
print(H)

for col in range(len(dish[0])):
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

summ = 0
for col in range(len(dish[0])):
    for row in range(H):
        if dish[row][col] == 'O':
            summ += H - row + 1
            
print(summ)

# < 111390