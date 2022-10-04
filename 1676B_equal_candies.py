# 1676B - Equal Candies
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    minimum = min(input_list)
    count = 0
    for j in range(n):
        count += input_list[j] - minimum

    print(count)