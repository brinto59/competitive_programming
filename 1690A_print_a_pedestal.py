# 1690A - print a pedestal
import math

t = eval(input())
for i in range(t):
    n = eval(input())
    h1 = math.ceil(n/3)
    h2 = h1
    h3 = h1
    # h1 and h3
    if n - (h1+h2+h3) < 0:
        h3 -= (h1+h2+h3) - n
    elif n - (h1+h2+h3) == 0:
        h1 += 1

    # h1 and h2
    if h1 == h2:
        h1 += 1
        h2 -= 1

    # h2 and h3
    if h2 == h3 and (h1+h2+h3) == n:
        h2 += 1
        h3 -= 1
    elif h2 == h3:
        h3 -= (h1+h2+h3) - n

    print(h2, h1, h3)

