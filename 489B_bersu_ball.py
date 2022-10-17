# 489B - Bersu ball
import math
n = eval(input())
boys_skill = list(map(lambda x: eval(x), input().split(" ")))
boys_skill.sort()
m = eval(input())
girls_skill = list(map(lambda x: eval(x), input().split(" ")))
girls_skill.sort()
partner_skill = []
smaller_group = []
larger = 0
isboy = bool
count = 0
between0and1 = False
if n > m:
    larger = n
    smaller_group.extend(girls_skill)
    partner_skill.extend([i, 'boy'] for i in boys_skill)
    isboy = True
else:
    larger = m
    smaller_group.extend(boys_skill)
    partner_skill.extend([i, 'girl'] for i in girls_skill)
    isboy = False

j = 0
k = 0
while j < len(smaller_group):
    if smaller_group[j] <= partner_skill[k][0] and between0and1 is False and ((isboy is True and partner_skill[k][1]=='boy') or (isboy is False and partner_skill[k][1]=='girl')):
        if isboy is True:
            partner_skill.insert(k, [smaller_group[j], 'girl'])
        else:
            partner_skill.insert(k, [smaller_group[j], 'boy'])

        if 0 <= (partner_skill[k+1][0] - smaller_group[j]) <= 1:
            between0and1 = True
        j += 1
    elif (k+1 < len(partner_skill)) and partner_skill[k][0] == partner_skill[k+1][0] and smaller_group[j]-partner_skill[k][0]==1:
        if isboy is True:
            partner_skill.insert(k+1, [smaller_group[j], 'girl'])
        else:
            partner_skill.insert(k+1, [smaller_group[j], 'boy'])
        j += 1
        between0and1 = False
    else:
        between0and1 = False
    if j == len(smaller_group):
        break
    if k == len(partner_skill) - 1:
        if isboy is True:
            partner_skill.insert(k+1, [smaller_group[j], 'girl'])
        else:
            partner_skill.insert(k+1, [smaller_group[j], 'boy'])
        break
    k += 1
i = 0
while i < len(partner_skill)-1:
    if ((partner_skill[i][1] == 'girl' and partner_skill[i+1][1] == 'boy') or (partner_skill[i][1] == 'boy' and
                                                                              partner_skill[i+1][1] == 'girl')) and \
            (0 <= math.fabs(partner_skill[i][0]-partner_skill[i+1][0]) <= 1):
        count += 1
        i += 2
    else:
        i += 1
print(count)