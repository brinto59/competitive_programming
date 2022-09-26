# 1294A - Collecting Coins

num = eval(input())
for i in range(num):
    input_str = list(map(lambda x: eval(x), input().split(" ")))
    n = input_str.pop()  # last element is the value of number of coins
    input_str.sort(reverse=True)  # sorting in descending order, first element is maximum
    for j in range(1, 3):
        n -= (input_str[0] - input_str[j])
        if n < 0:
            print("NO")
            break
    else:
        if n % 3 == 0:
            print("YES")
        else:
            print("NO")
