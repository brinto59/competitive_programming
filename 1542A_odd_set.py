# 1542A - Odd set
import math
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x) % 2, input().split(" ")))
    if math.fsum(input_list) == n:
        print("YES")
    else:
        print("NO")
