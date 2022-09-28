# 1353B - Two arrays and swaps
import math
t = eval(input())
temp = 0
for i in range(t):
    length_k = list(map(lambda x: eval(x), input().split(" ")))
    arr_1 = list(map(lambda x: eval(x), input().split(" ")))
    arr_2 = list(map(lambda x: eval(x), input().split(" ")))
    arr_1.sort()
    arr_2.sort(reverse=True)
    for j in range(length_k[1]):
        if arr_2[j] > arr_1[j]:
            temp = arr_1.pop(j)
            arr_1.insert(j, arr_2[j])
            arr_2.pop(j)
            arr_2.insert(j, temp)

    print(int(math.fsum(arr_1)))
