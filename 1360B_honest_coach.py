# 1360B -Honest Coach

t = eval(input())
for i in range(t):
    n = eval(input())
    strength_arr = list(map(lambda x: eval(x), input().split(" ")))
    strength_arr.sort()
    strength_diff_arr = []
    for j in range(len(strength_arr)-1):
        strength_diff_arr.append(strength_arr[j+1]-strength_arr[j])
    print(min(strength_diff_arr))