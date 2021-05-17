n,m=map(int,input().split())
l=[int(i) for i in input().split()]

if n!=m:
    print('ERREUR')
    exit()

if (n*(n+1))//2 !=sum(l):
    print('ERREUR')
else:
    print('OK')