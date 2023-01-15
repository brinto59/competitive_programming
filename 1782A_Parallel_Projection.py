# 1782A - Parallel Projection
import math
n = eval(input())
for i in range(n):
    w, d, h = list(map(lambda x: eval(x), input().split(' ')))
    a, b, f, g = list(map(lambda x: eval(x), input().split(' ')))
    min_dis = []
    # for a
    min_dis.append(a+h+f+int(math.fabs(g-b)))
    # for w-a
    min_dis.append(w-a+w-f+h+int(math.fabs(g-b)))
    # for b
    min_dis.append(b+h+g+int(math.fabs(f-a)))
    # for w-b
    min_dis.append(d-b + h + d-g + int(math.fabs(f - a)))
    print(min(min_dis))





