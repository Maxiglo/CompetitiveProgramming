n = int(input())
s=0
s2=0
for i in range(n):
    a,b= map(int,input().split())
    a = a*60
    s+=a
    s2+=b

temps = (s2/s)
if temps >1:
    print(temps)
else:
    print('measurement error')