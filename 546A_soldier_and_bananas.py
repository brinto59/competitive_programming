# 546A - Soldier and Bananas
import math

input_list = input().split(" ")
total_price = 0
for i in range(1, eval(input_list[2])+1):
    total_price += i

borrow_money = eval(input_list[0])*total_price - eval(input_list[1])
if borrow_money > 0:
    print(borrow_money)
else:
    print(0)

