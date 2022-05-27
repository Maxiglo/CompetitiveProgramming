import math 

n = int(input())
l = [int(i) for i in input().split()]
gcd = [math.gcd(i,l[0]) for i in l]
repn = [int(l[0]/gcd[i]) for i in range(len(l))]
rep = [int(l[i]/gcd[i]) for i in range(len(l))]

for i in range(1,len(l)):
    print(f'{repn[i]}/{rep[i]}')

