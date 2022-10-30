# 1560B - Who's Opposite?
t = eval(input())
for i in range(t):
    a, b, c = list(map(lambda x: eval(x), input().split(" ")))
    maximum = 0
    minimum = 0
    if a > b:
        maximum = a
        minimum = b
    else:
        maximum = b
        minimum = a

    person_each_side = maximum - minimum - 1
    person_before_min = minimum - 1  # number of person on the anticlockwise direction of the minimum number
    if (person_each_side == 0) or (person_before_min > person_each_side):
        print(-1)
        continue
    person_after_max = person_each_side - person_before_min  # number of person on the clockwise direction of the
    # maximum number
    total_person = person_after_max + maximum
    if (total_person % 2 != 0) or (c > total_person) :
        print(-1)
        continue
    if c > total_person/2:
        print(c-total_person//2)
    else:
        print(c+total_person//2)