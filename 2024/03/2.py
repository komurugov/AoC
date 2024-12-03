import re, sys

On = True
Sum = 0

for line in sys.stdin:
    for occurence in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', line):
        #print(occurence, occurence.lastindex)
        match occurence.lastindex:
            case 2:
                if On:
                    larg = occurence.group(1)
                    rarg = occurence.group(2)
                    Sum += int(larg) * int(rarg)
            case 3:
                On = True
            case 4:
                On = False

print(Sum)