# 1399A - Remove smallest
t = eval(input())
for i in range(t):
    n = eval(input())
    arr = list(map(lambda x: eval(x), input().split(" ")))
    # bubble sort
    for j in range(n):
        for k in range(n - 1):
            if arr[k] > arr[k + 1]:
                arr[k + 1], arr[k] = arr[k], arr[k + 1]
    p = 0
    q = 1
    for j in range(n-1):
        if not(0 <= arr[q] - arr[p] <= 1):
            print("NO")
            break
        p += 1
        q += 1
    else:
        print("YES")
