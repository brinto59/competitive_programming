# 1389A - LCM problem

t = eval(input())
for i in range(t):
    l_r = list(map(lambda x: eval(x), input().split(" ")))
    x = l_r[0]
    y = 2 * l_r[0]
    if y <= l_r[1]:
        print(x, y)
    else:
        print(-1, -1)
