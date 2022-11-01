# 1537A - Arithmetic Array
import math
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    total_sum = math.fsum(input_list)
    if total_sum < n:
        print(1)
    else:
        print(int(total_sum - n))
