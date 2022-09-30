# 1520B - Ordinary Numbers
t = eval(input())
for i in range(t):
    n = eval(input())
    count = 0
    for j in range(1, 10):
        k = 1
        result = 0
        while True:
            result += j*k
            if result <= n:
                count += 1
            else:
                break
            k *= 10
    print(count)
