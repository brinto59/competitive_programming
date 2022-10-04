# 9A - Die Roll
y_w = list(map(lambda x: eval(x), input().split(" ")))
max_value = max(y_w)
wining_rolls_num = 6 - max_value + 1
for i in range(6, 1, -1):
    if wining_rolls_num % i == 0 and 6 % i == 0:
        print(f"{int(wining_rolls_num/i)}/{int(6/i)}")
        break
else:
    print(f"{wining_rolls_num}/6")

