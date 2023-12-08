import sys

commands = input()

input()

network = {}

for line in sys.stdin:
    key = line[3]
    left = line[7:10]
    right = line[12:15]
    network[key] = { 'L': left, 'R': right }
    
i = 0
node = 'AAA'
while True:
    node = network[node][commands[i]]
    i += 1
    if node == 'ZZZ':
        break
        
print(i)