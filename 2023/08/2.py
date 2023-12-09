import sys

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