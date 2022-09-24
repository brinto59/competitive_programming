# 158A - Next round

[n, k] = list(map(lambda x: eval(x), input().split(" ")))

score = list(map(lambda x: eval(x), input().split(" ")))

print(len(list(filter(lambda x: (x >= score[k-1]) and (x > 0), score))))
# participant number who will advance to the next round
