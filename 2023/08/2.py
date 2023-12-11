import sys, math

commands = []
line = input()
for ch in line:
    if ch == 'L':
        commands.append(0)
    else:
        commands.append(1)
        
print(len(commands))

input()

network = []
nodes = []
node = 0
dic = {}

def GetNode(st):
    global node
    if st in dic:
        return dic[st]
    else:
        dic[st] = node
        node += 1
        return node - 1

def FindCycle(node):
    states = [(node, 0)]
    cycle = []
    i = 0
    j = 0
    while True:
        node = network[node][commands[i]]
        i += 1
        if i >= len(commands):
            i = 0
        j += 1
        try:
            pos = states.index((node, i))
            break
        except ValueError:
            states.append((node, i))
    prev = 0
    for i in range(pos, len(states)):
        if not network[states[i][0]][2]:
            cycle.append(i - prev)
            prev = i
    first = cycle[0]
    cycle[0] = len(states) - prev + first - pos
    return (cycle, first)

for line in sys.stdin:
    #print(line)
    key = GetNode(line[:3])
    left = GetNode(line[7:10])
    right = GetNode(line[12:15])
    if key >= len(network):
        network += [(0, 0, False)] * (key - len(network) + 1)
    network[key] = (left, right, line[2] != 'Z')
    
    if line[2] == 'A':
        nodes.append(key)
print(dic)
print(network)
print(nodes)

cycles = []
curs = []
mx = -1
res = 1
for n in nodes:
    cycles.append(FindCycle(n))
for n in cycles:
    res *= n[0][0]
    curs.append([0, n[1]])
    if n[1] > mx:
        mx = n[1]     

print(cycles)

nums = [c[1] for c in cycles]
print(math.lcm(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]))
  
exit()       
        
N = len(curs)
while True:
    end = True
    for n in range(N):
        while curs[n][1] < mx:
            #print('curs ', curs[n][1])
            curs[n][0] += 1
            if curs[n][0] >= len(cycles[n][0]):
                curs[n][0] = 0
            curs[n][1] += cycles[n][0][curs[n][0]]
        if curs[n][1] > mx:
            end = False
            mx = curs[n][1]
    #print(mx)
    if end:
        break
        
print(mx)

    
     
    

    
exit()
    
i = 0
j = 0
jj = 0
while True:
    end = True
    cmd = commands[i]
    for k in range(len(nodes)):
        net = network[nodes[k]]
        if net[2]:
            end = False
        nodes[k] = net[cmd]
    #print(nodes)
    if end:
        break
    i += 1
    j += 1
    if i >= len(commands):
        i = 0
        jj += 1
        if jj > 1000:
            jj = 0
            print(j)
    #print(nodes)
        
print(j)

# > 100000000
# != 26559759536163661731943307