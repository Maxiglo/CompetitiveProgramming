n = int(input())

if (n%2)!=0:
    print((n*n//2)+1)
else: print(n*n//2)
for i in range(n):
    rep=''
    for j in range(n):
        if i %2==0:
            if j%2==0:
                rep+='C'
            else:
                rep+='.'
        else:
            if j%2!=0:
                rep+='C'
            else:
                rep+='.'
    
    print(rep)