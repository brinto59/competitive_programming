# 266B - Queue at the school
import re
n_t = list(map(lambda x: eval(x), input().split(' ')))
child_queue = re.findall('[BG]', input())

for i in range(n_t[1]):
    j = 0
    while j < (n_t[0]-1):
        if child_queue[j] == 'B' and child_queue[j+1] == 'G':
            child_queue[j], child_queue[j+1] = child_queue[j+1], child_queue[j]
            j += 2
        else:
            j += 1
print("".join(child_queue))
