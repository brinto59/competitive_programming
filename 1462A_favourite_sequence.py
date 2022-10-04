# 1462A - Favourite Sequence
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = input().split(" ")
    output_list = []
    p = 0
    q = n-1
    for j in range(1, n+1):
        if j % 2 == 1:
            output_list.append(input_list[p])
            p += 1
        else:
            output_list.append(input_list[q])
            q -= 1
    print(" ".join(output_list))