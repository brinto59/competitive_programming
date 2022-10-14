# 1703B - ICPC Balloons

t = eval(input())
for i in range(t):
    n = eval(input())
    s = input()
    compare_list = []
    num_of_balloon = 0
    for j in range(n):
        if s[j] not in compare_list:
            num_of_balloon += 2
            compare_list.append(s[j])
        else:
            num_of_balloon += 1
    print(num_of_balloon)
