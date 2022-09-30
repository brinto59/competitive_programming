# 1472 - Fair Division
import math
t =eval(input())
for i in range(t):
    n =eval(input())
    candies_list = list(map(lambda x: eval(x), input().split(" ")))
    if math.fsum(candies_list) % 2 == 1:
        print("NO")
        continue
    num_two = candies_list.count(2)
    num_one = len(candies_list) - num_two
    if num_one % 2 == 0 and num_one != 0:
        print("YES")
        continue
    elif num_two % 2 == 0 and num_two != 0:
        print("YES")
    else:
        print("NO")
