# 732A - Buy a shovel
k_r = list(map(lambda x: eval(x), input().split(" ")))
n = 1
while True:
    result = (n*k_r[0]) % 10
    if result == 0:
        print(n)
        break
    if int(result/k_r[1]) == 1 and result % k_r[1] == 0:
        print(n)
        break
    n += 1
