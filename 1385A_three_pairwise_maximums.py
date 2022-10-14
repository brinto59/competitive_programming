# 1385A - three pairwise maximums
t = eval(input())
for i in range(t):
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    maximum = max(input_list)
    minimum = min(input_list)
    count = input_list.count(maximum)
    if count < 2:
        print("NO")
    else:
        print("YES")
        if count == 3:
            print(maximum, maximum, maximum)
        elif minimum-1 > 0:
            print(maximum, minimum, minimum-1)
        else:
            print(maximum, minimum, minimum)
