# 281A capitalization

string = input()
l = []
for i in range(len(string)):
    l.append(string[i])

l[0] = l[0].capitalize()
print("".join(l))
