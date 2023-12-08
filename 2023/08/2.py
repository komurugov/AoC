import sys

commands = input()

input()

network = {}
nodes = []

for line in sys.stdin:
    #print(line)
    key = line[:3]
    left = line[7:10]
    right = line[12:15]
    network[key] = { 'L': left, 'R': right }
    
    if key[2] == 'A':
        nodes.append(key)
#print(network)
    
i = 0
j = 0
while True:
    end = True
    for k in range(len(nodes)):
        node = network[nodes[k]][commands[i]]
        nodes[k] = node
        if node[2] != 'Z':
            end = False
    #print(node)
    i += 1
    j += 1
    if End:
        break
    if i >= len(commands):
        i = 0
        
print(j)
