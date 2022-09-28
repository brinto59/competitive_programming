# 32B - Borze

borze_code = input()
index = 0
while True:
    if borze_code[index] == '.':
        print('0', end="")
    else:
        index += 1
        if borze_code[index] == '.':
            print('1', end="")
        else:
            print('2', end="")
    index += 1
    if index == len(borze_code):
        break
