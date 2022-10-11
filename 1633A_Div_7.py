# 1633A - Div .7
t = eval(input())
for i in range(t):
    n = eval(input())
    if n % 7 == 0:
        print(n)
        continue
    r = n % 7
    if (n % 10) + (7 - r) <= 9:
        print(n + (7-r))
    else:
        print(n - r)

