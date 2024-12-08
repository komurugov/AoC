import sys

def IsWordDetected(array, startRow, startColumn, dir, word):
    for i in range(len(word)):
        row = startRow + i * dir[0]
        column = startColumn + i * dir[1]
        if row < 0 or row >= len(array) or column < 0 or column >= len(array[row]):
            return False
        if array[row][column] != word[i]:
            return False
    return True

Dirs = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

Rows = [line for line in sys.stdin]

Count = 0

for row in range(len(Rows)):
    for column in range(len(Rows[row])):
        for dir in Dirs:
            if IsWordDetected(Rows, row, column, dir, 'XMAS'):
                Count += 1

print(Count)