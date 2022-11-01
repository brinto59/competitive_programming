# 1368A - C+=
t = eval(input())
for i in range(t):
    a, b, n = list(map(lambda x: eval(x), input().split(" ")))
    count = 0
    if (a > n) or (b > n):
        print(count)
        continue
    while True:
        if a < b:
            a += b
        else:
            b += a
        count += 1
        if (a > n) or (b > n):
            break
    print(count)
