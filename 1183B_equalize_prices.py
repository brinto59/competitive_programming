# 1183B - Equalize Prices
import math

num_of_queries = eval(input())
list_input = []
new_price = 0

for i in range(num_of_queries):
    input1 = list(map(lambda x: eval(x), input().split(" ")))
    input2 = list(map(lambda x: eval(x), input().split(" ")))
    list_input.append({'n': input1[0], 'k': input1[1], 'prices': input2})

    minimum = min(list_input[i]['prices'])
    maximum = max(list_input[i]['prices'])
    new_price = minimum + list_input[i]['k']
    for j in range(minimum + list_input[i]['k'], 0, -1):
        if math.fabs(new_price - maximum) > list_input[i]['k']:
            print(-1)
            break
        elif math.fabs(maximum - new_price) <= list_input[i]['k'] and math.fabs(minimum - new_price) <= list_input[i][
            'k']:
            print(new_price)
            break
        else:
            new_price -= 1
