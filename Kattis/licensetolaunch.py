import sys 
n = input()

texte = list(map(int,input().split()))

m = min(texte)
pos = 0
for i in range(len(texte)):
    if texte[i]==m:
        pos=i
        break
print(pos)