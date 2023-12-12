import sys, datetime

cntres = 0
lengths = []
curar = []
src = ''

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
    

def proc(curlen, n, i):
    if (curlen != 0):
        if curar[curlen-1] == '#':
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
    if curlen == len(src):
        if curar[curlen-1] == '#':
            if n == lengths[i] and i == len(lengths) - 1:
                cntres += 1
        else:
            if i == len(lengths):
                cntres += 1
    else:
        ch = src[curlen]
        if ch == '?':
            curar[curlen] = '.'
            proc(curlen + 1, n, i)
            curar[curlen] = '#'
            proc(curlen + 1, n, i)
        else:
            curar[curlen] = ch
            proc(curlen + 1, n, i)



summ = 0
k = 0
for line in sys.stdin:
    line = line.split()
    src = line[0]
    lengths = list(map(int, line[1].split(',')))
    print(datetime.datetime.now().time(), src, lengths)
    curar = [' '] * len(src)
    proc(0, 0, 0)
    summ += cntres
    print(datetime.datetime.now().time(), k, ':', cntres, summ)
    cntres = 0
    k += 1
    
exit()
print(summ)    
    