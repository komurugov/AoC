import sys

def IsWordDetected(array, startRow, startColumn, dir, word):
    for i in range(len(word)):
        j = i - len(word) // 2
        row = startRow + j * dir[0]
        column = startColumn + j * dir[1]
        if row < 0 or row >= len(array) or column < 0 or column >= len(array[row]):
            return False
        if array[row][column] != word[i]:
            return False
    return True

Dirs = ((1, 1), (-1, 1))

Rows = [line for line in sys.stdin]

Count = 0

for row in range(len(Rows)):
    for column in range(len(Rows[row])):
        sides = 0
        for dir in Dirs:
            if IsWordDetected(Rows, row, column, dir, 'MAS') or IsWordDetected(Rows, row, column, dir, 'SAM'):
                sides += 1
            if sides == len(Dirs):
                Count += 1

print(Count)