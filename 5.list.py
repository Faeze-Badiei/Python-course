import random

s=int(input("enter number that you want in your list: "))
s_list=[]

for i in range(s):
    p=(random.randint(1,500))
    if p not in s_list:
        s_list.append(p)

print(s_list)
