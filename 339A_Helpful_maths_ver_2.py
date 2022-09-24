def match(arg):
    input_data = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    return input_data.get(arg)


string = input()
input_list = []

for i in range(len(string)):
    if string[i].isnumeric():
        input_list.append(match(string[i]))


input_list.sort()
input_list = list(map(lambda x: str(x), input_list))
print("+".join(input_list))