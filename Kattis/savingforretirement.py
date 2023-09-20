a,b,c,d,e=map(int,input().split())
bobsavings=(b-a)*c
s=0
for i in range(1000000):
    s+=e
    if s>bobsavings:
        print(d+i+1)
        break