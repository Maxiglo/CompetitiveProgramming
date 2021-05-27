n=int(input())
c=0
for _ in range(n):
    a,b=map(int,input().split(':'))
    if a>=20 or a<8:
        c+=1

if c>=n/2:
    print('SUSPICIOUS')
else:
    print('OK')