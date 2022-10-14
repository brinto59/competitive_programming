# 1579A - Casimir's String Solitaire
t = eval(input())
for i in range(t):
    input_str = input()
    count_a = input_str.count("A")
    count_b = input_str.count("B")
    count_c = input_str.count("C")
    if count_b - count_a == count_c:
        print("YES")
    else:
        print("NO")
