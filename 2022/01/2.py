import math, sys

sum = 0
max = [0, 0, 0]

for line in sys.stdin:
    if line != "\n":
        x = int(line)
        sum += x
    else:
        for i in range(0, 3):
            if sum > max[i]:
                if i < 2:
                    for j in range(2, i, -1):
                        max[j] = max[j - 1]
                max[i] = sum
                break
        sum = 0

print(max[0] + max[1] + max[2])
