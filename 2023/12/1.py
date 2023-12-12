import sys

cntres = 0
lengths = []

def compl(cur, lens):
    n = 0
    j = 0
    for i in range(len(cur)):
        if cur[i] == '#':
            n += 1
        else:
            if n != 0:
                if j >= len(lens) or n != lens[j]:
                    return False
                n = 0
                j += 1
    if n != 0:
        return j == len(lens) - 1 and n == lens[-1]
    return j == len(lens)
    

def proc(cur, src):
    global cntres
    if len(cur) == len(src):
        if compl(cur, lengths):
            cntres += 1
    else:
        ch = src[len(cur)]
        if ch == '?':
            proc(cur + ['.'], src)
            proc(cur + ['#'], src)
        else:
            proc(cur + [ch], src)

summ = 0
for line in sys.stdin:
    line = line.split()
    src = line[0]
    lengths = list(map(int, line[1].split(',')))
    proc([], src)
    summ += cntres
    cntres = 0
    
print(summ)    
    