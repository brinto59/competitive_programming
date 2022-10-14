# 731A - Night at the museum
import math
embosser = {'a': [1, -25],
            'b': [2, -24],
            'c': [3, -23],
            'd': [4, -22],
            'e': [5, -21],
            'f': [6, -20],
            'g': [7, -19],
            'h': [8, -18],
            'i': [9, -17],
            'j': [10, -16],
            'k': [11, -15],
            'l': [12, -14],
            'm': [13, -13],
            'n': [14, -12],
            'o': [15, -11],
            'p': [16, -10],
            'q': [17, -9],
            'r': [18, -8],
            's': [19, -7],
            't': [20, -6],
            'u': [21, -5],
            'v': [22, -4],
            'w': [23, -3],
            'x': [24, -2],
            'y': [25, -1],
            'z': [26, 0]
            }
input_str = input()
count = 0
current_pos = [1, -25]
for i in range(len(input_str)):
    if math.fabs(embosser[input_str[i]][0] - current_pos[0]) <= min(math.fabs(embosser[input_str[i]][1] - current_pos[0]),
                                                                    math.fabs(embosser[input_str[i]][0] - current_pos[1]),
                                                                    math.fabs(embosser[input_str[i]][1] - current_pos[1])):
        count += math.fabs(embosser[input_str[i]][0] - current_pos[0])
    elif math.fabs(embosser[input_str[i]][0] - current_pos[1]) <= min(math.fabs(embosser[input_str[i]][0] - current_pos[0])
                                                                , math.fabs(embosser[input_str[i]][1] - current_pos[0])
                                                                , math.fabs(embosser[input_str[i]][1] - current_pos[1])):
        count += math.fabs(embosser[input_str[i]][0] - current_pos[1])
    elif math.fabs(embosser[input_str[i]][1] - current_pos[0]) <= min(math.fabs(embosser[input_str[i]][0] - current_pos[0])
                                                                , math.fabs(embosser[input_str[i]][0] - current_pos[1])
                                                                , math.fabs(embosser[input_str[i]][1] - current_pos[1])):
        count += math.fabs(embosser[input_str[i]][1] - current_pos[0])
    elif math.fabs(embosser[input_str[i]][1] - current_pos[1]) <= min(math.fabs(embosser[input_str[i]][1] - current_pos[0])
                                                                , math.fabs(embosser[input_str[i]][0] - current_pos[1])
                                                                , math.fabs(embosser[input_str[i]][0] - current_pos[0])):
        count += math.fabs(embosser[input_str[i]][1] - current_pos[1])

    current_pos = embosser[input_str[i]]

print(int(count))

