# 1296A - Array with Odd sum
import math
t = eval(input())
for i in range(t):
    n = eval(input())
    a = list(map(lambda x: eval(x) % 2, input().split(" ")))
    if int(math.fsum(a)) % 2 == 1:
        print("YES")
    elif (math.fsum(a) / n == 1 and n % 2 == 0) or math.fsum(a) == 0:
        print("NO")
    else:
        print("YES")

