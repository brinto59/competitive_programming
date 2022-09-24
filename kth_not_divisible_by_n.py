num = eval(input())
for i in range(num):
    input_str = input()
    input_list = input_str.split(" ")
    input_list = list(map(lambda x: eval(x), input_list)).copy()
    n = input_list[0]
    k = input_list[1]

    if n > k:
        print(k)
    elif n == k:
        print(n+1)
    else:
        if k % (n-1) != 0:
            print(n*int(k/(n-1)) + k % (n-1))
        else:
            print(n*int(k/(n-1)) - 1)


