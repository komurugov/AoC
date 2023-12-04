import sys

game = 0
sum = 0

for line in sys.stdin:
    game += 1
    ok = True
    content = line.split(':')[1]
    sets = content.split(';')
    for set in sets:
        colors = set.split(',')
        for color in colors:
            cnt = int(color.split()[0])
            if color.find('red') > -1:
                if cnt > 12:
                    ok = False
            if color.find('green') > -1:
                if cnt > 13:
                    ok = False
            if color.find('blue') > -1:
                if cnt > 14:
                    ok = False
        if not ok:
            break
    if ok:            
        sum += game
        
print(sum)