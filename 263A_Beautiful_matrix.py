# 263A - Beautiful Matrix
input_list = []
m = 0  # row number of 1
n = 0  # column number of 1
for i in range(5):
    input_list.append(list(map(lambda x: eval(x), input().split(' '))))
    if input_list[i].count(1):
        n = input_list[i].index(1) + 1
        m = i + 1

m = m - 3
n = n - 3
print((m if m > 0 else -m) + (n if n > 0 else -n))
