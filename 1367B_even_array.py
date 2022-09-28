# 1367B - Even Array
t = eval(input())
count = 0
count_1 = 0
count_0 = 0
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x)%2, input().split(" ")))
    for j in range(n):
        if j % 2 != input_list[j]:
            count += 1
        if input_list[j] == 1:
            count_1 += 1
        else:
            count_0 += 1
    if count % 2 == 1 or count_1 != int(n/2) or count_0 != int((n-1)/2+1):
        print(-1)
    else:
        print(int(count/2))
    count = 0
    count_1 = 0
    count_0 = 0

