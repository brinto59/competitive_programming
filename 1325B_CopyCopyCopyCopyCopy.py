# 1325B - CopyCopyCopyCopyCopy
t = eval(input())
for i in range(t):
    n = eval(input())
    input_list = list(map(lambda x: eval(x), input().split(" ")))
    input_list.sort()
    j = 0
    while j < n-1:
        if input_list[j] == input_list[j+1]:
            input_list.pop(j)
            n -= 1
        else:
            j += 1
    print(len(input_list))
