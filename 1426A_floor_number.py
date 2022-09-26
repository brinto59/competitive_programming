# 1426A - Floor Number
import math

for i in range(eval(input())):
    input_str = list(map(lambda x: eval(x), input().split(" ")))

    if (input_str[0] >= 1) and (input_str[0] <= 2):
        print(1)
    else:
        print((math.ceil((input_str[0]-2)/input_str[1]) + 1))