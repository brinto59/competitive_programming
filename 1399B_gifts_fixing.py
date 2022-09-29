# 1399B - Gifts Fixing
t = eval(input())
count = 0
for i in range(t):
    n = eval(input())
    list_a = list(map(lambda x: eval(x), input().split(" ")))
    list_b = list(map(lambda x: eval(x), input().split(" ")))
    min_a = min(list_a)
    min_b = min(list_b)
    result = 0
    for j in range(n):
        if (list_b[j]-min_b) > (list_a[j]-min_a):
            result = list_b[j] - min_b
        else:
            result = list_a[j] - min_a
        count += result
    print(count)
    count = 0

