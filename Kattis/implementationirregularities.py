import math
n = int(input())
l=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]

z=sorted(list(zip(l,x)), key=lambda x:x[1])

rep=0
dem=0
for (a,b) in z:
    if b!=-1:
        dem+=a
        rep=max(rep, math.ceil(dem/b)) 
print(rep)