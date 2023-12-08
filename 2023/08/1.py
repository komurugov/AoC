import sys

commands = input()

input()

network = {}

for line in sys.stdin:
    #print(line)
    key = line[:3]
    left = line[7:10]
    right = line[12:15]
    network[key] = { 'L': left, 'R': right }
#print(network)
    
i = 0
j = 0
node = 'AAA'
while True:
    node = network[node][commands[i]]
    #print(node)
    i += 1
    j += 1
    if node == 'ZZZ':
        break
    if i >= len(commands):
        i = 0
        
print(j)
