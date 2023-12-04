import sys

sum = 0
cards = [1] * 204
n = -1

for line in sys.stdin:
    n += 1
    sum += cards[n]
    cnt = 0
    payload = line.split(':')[1].split('|')
    good = payload[0].split()
    have = payload[1].split()
    for num in have:
        if num in good:
            cnt += 1
    for i in range(n + 1, n + 1 + cnt):
        cards[i] += cards[n]

print(sum)