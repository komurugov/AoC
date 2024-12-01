import sys

LeftList = []
RightList = []

for line in sys.stdin:
    left, right = [int(s) for s in line.split()]
    LeftList.append(left)
    RightList.append(right)

LeftList.sort()
RightList.sort()

TotalDistance = 0
for i in range(0, len(LeftList)):
    TotalDistance += abs(LeftList[i] - RightList[i])

print(TotalDistance)