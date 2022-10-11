# 1506A - Strange Table
import math
t = eval(input())
for i in range(t):
    n_m_x = list(map(lambda x: eval(x), input().split(" ")))
    row = n_m_x[2] % n_m_x[0]
    if row == 0:
        row = n_m_x[0]
    col = math.ceil(n_m_x[2]/n_m_x[0])
    result = col + (row - 1)*n_m_x[1]
    print(result)