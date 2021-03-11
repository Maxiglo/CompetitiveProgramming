a,b,c,n = map(int,input().split())

if a ==0 or b==0 or c ==0:
    print('NO')
elif a+b+c>=n and n>=3:
    print('YES')
else: print('NO')