# 160A - Twins
def sum_of_coin_value(arg_list, num):
    s = 0
    for i in range(num):
        s += arg_list[i]
    return s


num_of_coins = eval(input())
coin_values = list(map(lambda x: eval(x), input().split(" ")))
coin_values.sort(reverse=True)
min_num = 0
min_value = 0
sum_val = sum_of_coin_value(coin_values, num_of_coins)

for i in range(num_of_coins):
    min_value += coin_values[i]
    min_num += 1
    if min_value > (sum_val - min_value):
        break

print(min_num)