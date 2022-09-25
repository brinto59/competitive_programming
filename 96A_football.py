# 96A Football

input_str = input()
s1 = 0
s0 = 0
for i in range(len(input_str)):
    if input_str[i] == '1':
        s1 += 1
        s0 = 0
        if s1 == 7:
            print("YES")
            break
    elif input_str[i] == '0':
        s0 += 1
        s1 = 0
        if s0 == 7:
            print("YES")
            break

if s1 < 7 and s0 < 7:
    print("NO")
