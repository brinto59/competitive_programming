# 509A - Maximum in table

n = eval(input())
n_by_n_list = []
maximum = 0
for i in range(n):
    row_list = []
    for j in range(n):
        if i == 0 or j == 0:
            row_list.append(1)
        else:
            row_list.append(row_list[j-1]+n_by_n_list[i-1][j])
    n_by_n_list.append(row_list)
    maximum = max(row_list)
print(maximum)