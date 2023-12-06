import math

T = int(''.join(input().split()[1:]))
L = int(''.join(input().split()[1:]))

a = 1
b = -T
c = L

D = b * b - 4 * a * c

x1 = math.ceil((-b - math.sqrt(D)) / (2 * a))
x2 = math.floor((-b + math.sqrt(D)) / (2 * a))

print(x2 - x1 + 1)
