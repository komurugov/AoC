import sys, datetime

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
    

def proc(cur, src, n, i):
    if (len(cur) != 0):
        if cur[-1] == '#':
            if n == 0:
                if i >= len(lengths):
                    return
            n += 1
            if n > lengths[i]:
                return
        else:
            if n != 0:
                if n < lengths[i]:
                    return
                i += 1
                n = 0
        
    global cntres
    if len(cur) == len(src):
        if cur[-1] == '#':
            if n == lengths[i] and i == len(lengths) - 1:
                cntres += 1
        else:
            if i == len(lengths):
                cntres += 1
    else:
        ch = src[len(cur)]
        if ch == '?':
            proc(cur + ['.'], src, n, i)
            proc(cur + ['#'], src, n, i)
        else:
            proc(cur + [ch], src, n, i)

summ = 0
k = 0
for line in sys.stdin:
    line = line.split()
    src = line[0]
    for i in range(4):
        src += '?' + line[0]
    lengths = list(map(int, line[1].split(','))) * 5
    #print(src, lengths)
    proc([], src, 0, 0)
    summ += cntres
    print(datetime.datetime.now().time(), k, ':', cntres)
    cntres = 0
    k += 1
    
print(summ)    
    