# 791A - Bear and Big Brother
import math

input_list = list(map(lambda x: eval(x), input().split(" ")))
y = math.floor(math.log(input_list[1]/input_list[0])/math.log(3/2)) + 1
print(y)