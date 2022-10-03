# 1353A -Most unstable Array

t = eval(input())
for i in range(t):
    n_m = list(map(lambda x: eval(x), input().split(" ")))
    print(min(2, n_m[0]-1)*n_m[1])
