# 112A - Petya and Strings
input_list = []
for i in range(2):
    input_list.append(input())
    input_list[i] = input_list[i].lower()

for i in range(len(input_list[0])):
    if input_list[0][i] > input_list[1][i]:
        print(1)
        break
    elif input_list[0][i] < input_list[1][i]:
        print(-1)
        break

if input_list[0][i] == input_list[1][i]:
    print(0)
