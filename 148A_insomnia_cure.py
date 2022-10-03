# 148A - Insomnia Cure
k_l_m_n_d = []
count = 0
for i in range(5):
    k_l_m_n_d.append(eval(input()))

for i in range(1, k_l_m_n_d[4]+1):
    for j in range(4):
        if i % k_l_m_n_d[j] == 0:
            count += 1
            break
        j += 1
print(count)