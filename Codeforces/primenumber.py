def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                npremier = False
                break
        else:
            npremier= True
    return npremier

a,b= map(int,input().split())
for j in range(a+1,b+1):
    
    if prime(j):
        rep= j
        break
    else:
        rep=0

if b==rep:
    print('YES')
else:
    print('NO')