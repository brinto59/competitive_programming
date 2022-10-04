# 1454A - Special Permutation
t = eval(input())
for i in range(t):
    n = eval(input())
    output_list = []
    k = 1
    p = n
    for j in range(0, n):
        if j < int(n / 2):
            output_list.append(f"{p}")
            p -= 1
        else:
            output_list.append(f"{k}")
            k += 1
    print(" ".join(output_list))
