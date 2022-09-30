# 1472B - Fair Division
import math
t = eval(input())
for i in range(t):
    n = eval(input())
    candies_list = list(map(lambda x: eval(x), input().split(" ")))
    candies_list.sort(reverse=True)

    if math.fsum(candies_list) % 2 == 1:
        print("NO")
        continue

    busket = [candies_list[0]]
    for j in range(1, n):
        if math.fsum(busket) + candies_list[j] < (math.fsum(candies_list)-math.fsum(busket)-candies_list[j]):
            busket.append(candies_list[j])
        elif math.fsum(busket) + candies_list[j] == (math.fsum(candies_list)-math.fsum(busket)-candies_list[j]):
            busket.append(candies_list[j])
            break
    if math.fsum(busket) == int(math.fsum(candies_list)/2):
        print('YES')
    else:
        print('NO')