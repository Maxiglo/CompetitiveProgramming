#easy, suffit de check k+1 dans la liste et  vérifier s'il est dans l'ordre
n = int(input())
for i in range(n):
    l = [int(j) for j in input().split()]
    for k in range(1,len(l)-1):
        if l[k+1]!=l[k]+1:
            pos= k
    
    print(pos)