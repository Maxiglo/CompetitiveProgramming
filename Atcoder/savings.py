n=int(input())
i=0
c=0
tot=0
for _ in range(100000000000):
    i+=1
    c+=1
    tot+=i
    if tot>=n:
        print(c)
        exit()