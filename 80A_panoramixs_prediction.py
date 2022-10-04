# 80A - Panoramix's Prediction

n_m = list(map(lambda x: eval(x), input().split(" ")))
i = n_m[0] + 1
isPrime = True
while True:
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime is True:
        break
    else:
        isPrime = True
        i += 1
if i == n_m[1]:
    print("YES")
else:
    print("NO")

