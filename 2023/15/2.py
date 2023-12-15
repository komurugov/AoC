line = input()
print(len(line), line[-1])
inp = line.split(',')
summ = 0
boxes = []
for i in range(256):
    boxes.append([])

for code in inp:
    ps = code.find('-')
    rmv = ps != -1
    if not rmv:
        ps = code.find('=')
        
    hsh = 0
    for ch in code[0:ps]:
        hsh = (hsh + ord(ch)) * 17 % 256
    
    if rmv:
        boxes[hsh] = [i for i in boxes[hsh] if i[0] != code[0:ps]]
    else:
        found = False
        for lens in boxes[hsh]:
            if lens[0] == code[0:ps]:
                found = True
                lens[1] = int(code[ps + 1:ps + 2])
        if not found:
            boxes[hsh].append([code[0:ps], int(code[ps + 1:ps + 2])])

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        summ += (i + 1) * (j + 1) * boxes[i][j][1]
        
print(boxes)
    
print(summ)

# > 214026