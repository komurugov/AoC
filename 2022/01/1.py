import math, sys
sum = 0
max = 0
for line in sys.stdin:
	if line != "\n":
		x = int(line)
		sum += x
	else:
		if sum > max:
			max = sum
		sum = 0
print(max)
			