# 282A - Bit++

n = eval(input())
x = 0
for i in range(n):
    string = input()
    for j in range(len(string)):
        if string[j] == "+":
            x += 1
            break
        elif string[j] == "-":
            x -= 1
            break

print(x)
