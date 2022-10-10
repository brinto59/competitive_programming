# 1529A - Eshag Loves Big Arrays
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda e: eval(e), input().split(" ")))
    minimum = min(input_list)
    minimum_count = input_list.count(minimum)
    print(n-minimum_count)