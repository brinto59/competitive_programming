# 1551A - polycrap and coins
t = eval(input())
for i in range(t):
    n = eval(input())
    k = 0
    c1 = 0
    c2 = 0
    while True:
        if (n+2*k) % 3 == 0:
            c1 = int((n+2*k)/3)
            c2 = c1 - k
            print(c1, c2)
            break
        elif (n-2*k) % 3 == 0:
            c1 = int((n-2*k)/3)
            c2 = c1 + k
            print(c1, c2)
            break
        k += 1
