n = int(input())
c=0
for i in range(n):
    ligne = [int(x) for x in input().split() ]
    if ligne.count(1)>=2:
        c+=1
print(c)