# 1722B - Colourblindness
import re
t = eval(input())
for i in range(t):
    n = eval(input())
    row1 = re.findall("[A-Za-z]", input())
    row2 = re.findall("[A-Za-z]", input())
    identical = True
    for j in range(n):
        if row1[j] == 'G' and row2[j] == 'B':
            identical = True
        elif row1[j] == 'B' and row2[j] == 'G':
            identical = True
        elif row1[j] != row2[j]:
            identical = False
            break
    print("YES" if identical is True else "NO")

