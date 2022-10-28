#  1722A - Spell Check
t = eval(input())
for i in range(t):
    isCorrect = False
    n = eval(input())
    name_str = input()
    desired_char = ['T', 'i', 'm', 'u', 'r']
    if len(name_str) != 5:
        print("NO")
        continue
    for j in name_str:
        if j in desired_char:
            isCorrect = True
            desired_char.remove(j)
        else:
            isCorrect = False
            break
    if isCorrect is True:
        print("YES")
    else:
        print("NO")
