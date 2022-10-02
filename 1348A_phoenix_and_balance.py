# 1348A - Phoenix and Balance
import math
t = eval(input())
for i in range(t):
    length = eval(input())
    input_list = []
    for j in range(1, length+1):
        input_list.append(2**j)
    result = math.fsum(input_list)
    sum_of_half = input_list[length-1]
    result -= input_list[length-1]
    for j in range(int(length/2)-1):
        sum_of_half += input_list[j]
        result -= input_list[j]

    print(int(math.fabs(result-sum_of_half)))