import sys

game = 0
sum = 0

for line in sys.stdin:
    game += 1
    ok = True
    maxR, maxG, maxB = 0, 0, 0
    content = line.split(':')[1]
    sets = content.split(';')
    for set in sets:
        colors = set.split(',')
        for color in colors:
            cnt = int(color.split()[0])
            if color.find('red') > -1:
                if cnt > maxR:
                    maxR = cnt
            if color.find('green') > -1:
                if cnt > maxG:
                    maxG = cnt
            if color.find('blue') > -1:
                if cnt > maxB:
                    maxB = cnt
    sum += maxR * maxG * maxB
        
print(sum)