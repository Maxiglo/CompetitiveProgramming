import math
n=int(input())
vmax=0
t0,d0=map(int,input().split())
for i in range(n-1):
    t,d=map(int,input().split())
    if (d-d0)/(t-t0)>vmax:
        vmax=(d-d0)/(t-t0)
    
    t0,d0=t,d 
print(math.floor(vmax))