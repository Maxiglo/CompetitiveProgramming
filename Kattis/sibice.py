import math
n,w,h= map(int,input().split())
hyp = math.sqrt(w**2+h**2)
for i in range(n):
    taille = int(input())
    if taille<=hyp:
        print("DA")
    else: print("NE")
    