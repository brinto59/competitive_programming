# 1490A - Dense Array
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    count = 0
    for j in range(n - 1):
        minimum = min(input_list[j], input_list[j + 1])
        maximum = max(input_list[j], input_list[j + 1])
        while minimum * 2 < maximum:
            minimum *= 2
            count += 1
    print(count)
