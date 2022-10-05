# 1372A - Omkar and Completion
t = eval(input())
for i in range(t):
    n = eval(input())
    output_list = []
    j = 1
    while j < (n+1):
        if (j+1) <= n:  # all odd integers follows the condition. You can also print only 1 that also satisfy the condition
            output_list.extend([f"{j}", f"{j}"])
        else:
            output_list.append(f"{j}")
        j += 2
    print(" ".join(output_list))
