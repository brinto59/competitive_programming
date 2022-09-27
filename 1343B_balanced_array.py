# 1343B - Balanced Array

t = eval(input())
output_list = []
even_list = []
odd_list = []
for i in range(t):
    n = eval(input())
    if (n / 2) % 2 != 0:
        print("NO")
    else:
        print("YES")
        k = 2
        for j in range(int(n / 4)):
            even_list.append(k)
            odd_list.append(k - 1)
            k += 2

        for j in range(int(n / 4)):
            even_list.append(k)
            odd_list.append(k + 1)
            k += 2

        output_list.extend(even_list)
        output_list.extend(odd_list)
        print(" ".join(list(map(lambda x: str(x), output_list))))
        output_list.clear()
        odd_list.clear()
        even_list.clear()