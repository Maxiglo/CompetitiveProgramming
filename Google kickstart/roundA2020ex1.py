n = int(input())

for i in range(n):
    a,b= map(int,input().split())
    l= [int(j) for j in input().split()]
    l.sort()
    somme = 0
    c=0
    
    for k in range(len(l)):
        if b>=l[k]:
            b-=l[k]
            c+=1
        else:
            break
    print('Case #'+str(i+1)+": "+str(c))