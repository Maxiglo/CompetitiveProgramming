import sys
input=sys.stdin.readline
a,b= map(int,input().split())
if a==0:
    print()
    exit()

l=[]

for i in range(a):
    ingredient = input().split()
    l.append(ingredient)

rep= l[0]
bad=[]
for i in range(1,len(l)):
    for elem in rep:
        if elem not in l[i]:
            bad.append(elem)     

if len((set(rep)-set(bad)))>0:
    print(len((set(rep)-set(bad))))
    repfinale=sorted((set(rep)-set(bad)))
    print(*repfinale)
else:
    print(0)
