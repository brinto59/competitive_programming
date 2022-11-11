t = eval(input())
for i in range(t):
    a, b = list(map(lambda x: eval(x), input().split(" ")))
    if a == 0:
        print(1)
    else:
        print(a*1 + b*2 + 1)