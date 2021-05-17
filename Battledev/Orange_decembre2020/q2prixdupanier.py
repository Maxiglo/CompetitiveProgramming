import math
n=int(input())
mtot=0
prix=0
for i in range(n):
    a,b,c=map(int,input().split())
    mtot+=int(a)*(c/1000)
    prix+=a*b

print(math.floor(495+(mtot*125)+prix))