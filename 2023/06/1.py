import math

Ts = list(map(int, input().split()[1:]))
Ls = list(map(int, input().split()[1:]))

R = 1

for i in range(len(Ts)):
    a = 1.0
    b = -1.0 * Ts[i]
    c = 1.0 * Ls[i]
    D = b * b - 4 * a * c
    t1 = math.ceil((-b - math.sqrt(D)) / (2 * a))
    if (Ts[i] - t1) * t1 == Ls[i]:
        t1 += 1
    t2 = math.floor((-b + math.sqrt(D)) / (2 * a))
    if (Ts[i] - t2) * t2 == Ls[i]:
        t2 -= 1
    r = t2 - t1 + 1
    R *= r
    print(t1, t2)
    
print(R)