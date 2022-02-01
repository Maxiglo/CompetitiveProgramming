n=int(input())
l=[]
for i in range(n):
    nom,taille=input().split()
    l.append([nom,int(taille)])

l=sorted(l,key=lambda x:x[1])

print(l[-2][0])