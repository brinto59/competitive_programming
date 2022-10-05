# 1337A - Ichihime and Triangle
t = eval(input())
for i in range(t):
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    x = input_list[1]
    y = input_list[2]
    z = input_list[2]
    # if x+y > z and y+z > x and x+z >y:  # it is always true
    print(x, y, z)
