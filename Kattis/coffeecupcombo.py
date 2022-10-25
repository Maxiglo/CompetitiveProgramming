n = int(input())

s = input()

cf=0
tot=0
for i in s:
    if i=='1':
        cf = 2
        tot+=1
    else:
        if cf>0:
            cf-=1
            tot+=1
print(tot)