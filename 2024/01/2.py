import sys

LeftList = []
RightList = []

for line in sys.stdin:
    left, right = [int(s) for s in line.split()]
    LeftList.append(left)
    RightList.append(right)

SimilarityScore = 0
for x in LeftList:
    SimilarityScore += x * RightList.count(x)

print(SimilarityScore)