n=int(input())

for _ in range(n):
    taille=int(input())
    l=[int(i) for i in input().split()]
    if sum(l)%taille!=0:
        print(-1)
    else:
        m=sum(l)/len(l)
        print(sum(map(lambda x:x>m,l)))