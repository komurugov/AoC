import math, sys

x = '0'
y = '0'
sum = 0

for line in sys.stdin:
	for ch in line:
		if ch >= '0' and ch <= '9':
			x = ch
			break
	for ch in line:
		if ch >= '0' and ch <= '9':
			y = ch
	sum += int(x + y)

print(sum)
