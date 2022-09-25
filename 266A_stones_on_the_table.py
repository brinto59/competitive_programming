# 266A stones on the table

num_of_stones = eval(input())
stones_clr = input()
min_stones = 0

for i in range(num_of_stones-1):
    if stones_clr[i] == stones_clr[i+1]:
        min_stones += 1

print(min_stones)
