line = input()
print(len(line), line[-1])
inp = line.split(',')
summ = 0
for code in inp:
    hsh = 0
    for ch in code:
        hsh = (hsh + ord(ch)) * 17 % 256
    summ += hsh
    
print(summ)