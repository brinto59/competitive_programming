# 599A - Patrick and Shopping
d1, d2, d3 = list(map(lambda x: eval(x), input().split(" ")))
d = 0
if d1<d2:
    d += d1
else:
    d += d2

if d3 < (d1+d2):
    d += d3
else:
    d += (d1+d2)
if d1 < d2:
    if d2 < (d1+d3):
        d += d2
    else:
        d += (d3+d1)
else:
    if d1 < (d2+d3):
        d += d1
    else:
        d += (d3+d2)
print(d)
