import math
n,m = [int(i) for i in input().split()]
c=0
for a in range(max(n,m)+1):
    for b in range(max(n,m)+1):
        if a**2+b==n and a+b**2==m:
            c+=1
print(c) 