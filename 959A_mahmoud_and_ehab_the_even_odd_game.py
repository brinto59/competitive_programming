# 959A - Mahmoud and Ehab and the even-odd game
n = eval(input())
mahmoud_turn = True
while True:
    if mahmoud_turn is True:
        if n <= 0:
            print("Ehab")
            break
        elif n % 2 == 0:
            a = n
        else:
            a = n-1
            if a <= 0:
                print("Ehab")
                break
        mahmoud_turn = False
        n -= a

    else:
        if n <= 0:
            print("Mahmoud")
            break
        elif n % 2 == 1:
            a = n
        else:
            a = n-1
            if a <= 0:
                print("Mahmoud")
                break
        mahmoud_turn = True
        n -= a
