import sys, math

CharWeights = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

def GetWeight(src):
    #print(src)
    w = 0
    
    p = 1
    for i in range(4, -1, -1):
        #print(i)
        w += CharWeights[src[i]] * p
        p *= 13
        
    src = list(src)
    src.sort()
    #print(src)
    
    jcnt = src.count('J')
    js = jcnt in range(1, 5)
    if js:
        src = [i for i in src if i != 'J']
    
    cnts = []
    cnt = 1
    for i in range(1, len(src)):
        if src[i] == src[i - 1]:
            cnt += 1
        else:
            cnts.append(cnt)
            cnt = 1
    cnts.append(cnt)
    
    cnts.sort(reverse = True)
    
    if js:
        cnts[0] += jcnt
    
    hw = GetHandWeight(cnts)
    #print(w, '+', hw)
    w += hw * math.pow(13, 6)
        
    return w
    

def GetHandWeight(cnts):
    if len(cnts) == 5:  #high card
        return 0
    if len(cnts) == 4:  #one pair
        return 1
    elif len(cnts) == 3:
        if cnts[0] == 2:    # two pair
            return 2
        else:               # three of a kind
            return 3
    elif len(cnts) == 2:
        if cnts[0] == 3:    # full house
            return 4
        else:               # four of a kind
            return 5
    elif len(cnts) == 1:    # five
        return 6
    print('error')
    
    
    
    

hands = []

def ZeroItem(lst):
    return lst[0]

for line in sys.stdin:
    weight = GetWeight(line[:5])
    hands.append((weight, int(line.split()[1])))
    
hands.sort(key = ZeroItem)
#print(hands)
sum = 0
for i in range(len(hands)):
    sum += (i + 1) * hands[i][1]
print(sum)

# > 248290391 < 250274911