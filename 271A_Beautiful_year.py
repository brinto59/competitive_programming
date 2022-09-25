# 271A - Beautiful year

y = eval(input())
nums = []
x = str
while True:
    y += 1
    x = str(y)
    for i in range(len(x)):
        if x[i] not in nums:
            nums.append(x[i])
    if len(nums) == 4:
        print("".join(nums))
        break
    else:
        nums.clear()


