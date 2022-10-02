# 1619A - Square string?

t = eval(input())
for i in range(t):
    input_str = input()
    if len(input_str) % 2 == 1:
        print("NO")
        continue
    for j in range(int(len(input_str)/2)):
        if input_str[j] != input_str[j+int(len(input_str)/2)]:
            print("NO")
            break
    else:
         print("YES")
