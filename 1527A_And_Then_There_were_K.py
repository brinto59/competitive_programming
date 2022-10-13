# 1527A - And Then There were K
t = eval(input())
for i in range(t):
    n = eval(input())
    k = 0
    r = 2**k
    while r < n:
        k += 1
        r += 2**k

    r -= 2**k  # subtracting the last value that did not fulfil the condition
    print(r)
