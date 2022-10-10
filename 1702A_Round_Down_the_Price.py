# 1702A - Round Down the Price
t = eval(input())
for i in range(t):
    m = input()
    d = eval(m) - 10**(len(m)-1)
    print(d)