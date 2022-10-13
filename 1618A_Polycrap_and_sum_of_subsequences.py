# 1618A - Polycrap and sum of subsequences
import math
t = eval(input())
for i in range(t):
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    j = 2
    output_list = [input_list[0], input_list[1]]  # sum of two numbers is greater than the two numbers
    input_list.remove(input_list[0]+input_list[1])
    while len(output_list) != 3:
        if output_list[1] + input_list[j] in input_list and math.fsum(output_list)+input_list[j] in input_list:
            output_list.append(input_list[j])
        else:
            j += 1

    print(" ".join(list(map(lambda x: str(x), output_list))))
