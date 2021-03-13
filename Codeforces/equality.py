n,k = map(int,input().split())
mot = input()

alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s= alphabet[:k]
l=[]
for elem in s:
    occ= mot.count(elem)
    l.append(occ)
l.sort()
#compter occurences de chaque lettre sous sequence dans le mot et multiplier par le nombre de lettres
print(l[0]*k)