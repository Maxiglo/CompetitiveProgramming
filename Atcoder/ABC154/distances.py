from math import sqrt
n,d=map(int,input().split())
c=0
for i in range(n):
    a,b=map(int,input().split())
    if sqrt(a**2+b**2)<=d:
        c+=1
print(c)