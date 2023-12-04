import sys

sum = 0

for line in sys.stdin:
    payload = line.split(':')[1].split('|')
    good = payload[0].split()
    have = payload[1].split()
    pwr = 0
    for num in have:
        if num in good:
           if pwr:
                pwr *= 2
           else:
                pwr = 1
    sum += pwr

print(sum)
    