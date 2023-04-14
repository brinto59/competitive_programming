# 996A - Hit the lottery
import sys
n = eval(input())
bills_list = [0, 100, 20, 10, 5, 1]
c = [
    [0]*6,
    [0]*6,
    [0]*6,
    [0]*6,
    [0]*6,
    [0]*6
]
minimum = sys.maxsize

for i in range(1, 6):
    r = n   # remainder
    for j in range(i, 6):
        c[i][j] = r//bills_list[j] + c[i][j-1]
        r = r % bills_list[j]
    if c[i][j] < minimum:
        minimum = c[i][j]

print(minimum)
