import math, sys

sum = 0
replaces = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

for line in sys.stdin:
	x = '0'
	y = '0'
	back = line

	digit = -1
	first = -1
	for i in range(0, len(replaces)):
		pos = line.find(replaces[i][0])
		if pos != -1 and (first == -1 or pos < first):
			first = pos
			digit = i
	if digit != -1:
		line = line.replace(replaces[digit][0], replaces[digit][1], 1)
	for ch in line:
		if ch >= '0' and ch <= '9':
			x = ch
			break

	line = back
	digit = -1
	first = -1
	for i in range(0, len(replaces)):
		pos = line.rfind(replaces[i][0])
		if pos != -1 and (first == -1 or pos > first):
			first = pos
			digit = i
	if digit != -1:
		line = line.replace(replaces[digit][0], replaces[digit][1])
	for ch in line:
		if ch >= '0' and ch <= '9':
			y = ch


	sum += int(x + y)

print(sum)

# > 54571