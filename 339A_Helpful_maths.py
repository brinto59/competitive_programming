# 339A - Helpful Maths

num = input().split("+")
length = len(num)
for i in range(length):
    for j in range(length - 1):
        if eval(num[j]) > eval(num[j+1]):
            num[j+1], num[j] = num[j], num[j+1]

num = "+".join(num)
print(num)

