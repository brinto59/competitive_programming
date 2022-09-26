# 1335A - Candies and Two sisters
t = eval(input())  # number of test cases
for i in range(t):
    n = eval(input())
    if n % 2 == 0:
        if int((n-1)/2) > 0:
            print(int((n-1)/2))
        else:
            print(0)
    else:
        if int(n/2) > 0:
            print(int(n/2))
        else:
            print(0)
