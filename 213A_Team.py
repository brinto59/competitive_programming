# 213A Team

n = eval(input())
k = 0
c = 0
for i in range(n):
    string = input()
    for j in range(len(string)):
        if string[j] == '1':
            c += 1
            if c >= 2:
                k += 1
                c = 0
                break
    c = 0
print(k)  # the number of problems they can solve

