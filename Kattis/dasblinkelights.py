import math
p,q,s = map(int,input().split())
ppcm = (p*q)//math.gcd(p,q)
if ppcm<=s:
    print("yes")
else:
    print("no")