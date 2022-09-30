# 1311A - Add Odd or Subtract Even

t = eval(input())
for i in range(t):
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    if input_list[0] < input_list[1]:
        if (input_list[1] - input_list [0])%2==0:
            print(2)
        else:
            print(1)
    elif input_list[0] > input_list[1]:
        if (input_list[0] - input_list[1]) % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        print(0)
