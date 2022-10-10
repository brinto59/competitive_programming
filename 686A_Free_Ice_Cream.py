# 686A - Free Ice Cream
n_x = list(map(lambda e: eval(e), input().split(" ")))
initial = n_x[1]
distressed = 0
for i in range(n_x[0]):
    input_list = input().split(" ")

    if input_list[0] == "-":
        if eval(input_list[1]) > initial:
            distressed += 1
        else:
            initial -= eval(input_list[1])
    else:
        initial += eval(input_list[1])

print(initial, distressed)
