import re, sys

MulInstructionsArgs = []

for line in sys.stdin:
    MulInstructionsArgs += re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)

Sum = 0

for larg, rarg in MulInstructionsArgs:
    Sum += int(larg) * int(rarg)

print(Sum)