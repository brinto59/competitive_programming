# 236A Boy or Girl

input_str = input()
distinct_char = []
for i in range(len(input_str)):
    if input_str[i] not in distinct_char:
        distinct_char.append(input_str[i])

if len(distinct_char) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
