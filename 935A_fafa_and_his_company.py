# 935A - Fafa and his company

n = eval(input())
count = 0
for i in range(1, int(n/2)+1):
    if (n-i) % i == 0:
        count += 1
print(count)