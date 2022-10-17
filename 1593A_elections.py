# 1593A - Elections
t = eval(input())
for i in range(t):
    input_list= list(map(lambda x:eval(x), input().split(" ")))
    maximum=max(input_list)
    for j in range(3):
         if input_list.count(maximum)>1and input_list[j]==maximum:
             print(1,end=" ")
         elif input_list[j]==maximum:
             print(0,end=" ")
         else:
              print(maximum-input_list[j]+1, end=" ")
    print()