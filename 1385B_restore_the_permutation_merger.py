# 1385B - Restore the permutation by Merger

t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = input().split(" ")
    output_list = []
    count = 1
    for j in range(len(input_list)):
        if input_list[j] not in output_list:
            output_list.append(input_list[j])
            count += 1
            if count > n:
                break
    print(" ".join(output_list))