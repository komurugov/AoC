import sys, datetime

cntres = 0
lengths = []
curar = []
src = ''
S = 0
L, LL = 0, 0

def compl():
    #print(curar)
    i = 0
    for j in range(L * 2 + 1):
        if j % 2 == 0:
            ch = '.'
            ex = curar[j // 2]
        else:
            ch = '#'
            ex = lengths[j // 2]
        for k in range(ex):
            if i >= len(src):
                return False
            if src[i] != ch and src[i] != '?':
                return False
            i += 1
    return i == len(src)    
    

def proc(curlen, ll, srclen):
    global cntres
    global curar
    #print(curlen, ll, curar)
    if curlen == L + 1:
        if ll == 0:
            cntres += 1
        return
    if ll == 0 and curlen < L:
        return
    if curlen == 0 or curlen == L:
        st = 0
    else:
        st = 1
    for i in range(st, ll + 2 - (L - curlen)):
        if srclen + i > S:
            return
        if src.find('#', srclen, srclen + i) != -1:
            return
        if curlen < L:
            if srclen + i + lengths[curlen] > S:
                return
            if src.find('.', srclen + i, srclen + i + lengths[curlen]) != -1:
                continue
        curar[curlen] = i
        proc(curlen + 1, ll - i, srclen + i + (lengths[curlen] if curlen < L else 0))

summ = 0
k = 0
for line in sys.stdin:
    line = line.split()
    src = line[0]
    S = len(src)
    lengths = list(map(int, line[1].split(',')))
    print(datetime.datetime.now().time(), src, lengths)
    L = len(lengths)
    LL = sum(lengths)
    curar = [0] * (len(lengths) + 1)
    proc(0, S - LL, 0)
    summ += cntres
    print(datetime.datetime.now().time(), k, ':', cntres, summ)
    cntres = 0
    k += 1
    
exit()
print(summ)    
    