# 702A - Maximum Increase
n = eval(input())
arr = list(map(lambda x: eval(x), input().split(" ")))
count = 1
maxPrevCount = 1
for i in range(0, n-1):
    if arr[i] < arr[i+1]:
        count += 1
        # print("count", count)
    else:
        if count > maxPrevCount:
            maxPrevCount = count
        count = 1
if count > maxPrevCount:
    maxPrevCount = count

print(maxPrevCount)
