# 1729A - Two Elevators
t = eval(input())
for i in range(t):
    a, b, c = list(map(lambda x: eval(x), input().split(" ")))
    time_taken_by_lift1 = a - 1
    if b > c:
        time_taken_by_lift2 = b - 1
    else:
        time_taken_by_lift2 = (c - b) + (c - 1)
    if time_taken_by_lift1 < time_taken_by_lift2:
        print(1)
    elif time_taken_by_lift1 > time_taken_by_lift2:
        print(2)
    else:
        print(3)
