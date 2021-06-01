s=input()

a=s[:len(s)//2].lower()
b=s[len(s)//2:].lower()

sA=sum(ord(c)-97 for c in a)
sB=sum(ord(c)-97 for c in b)

newA=''
newB=''
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
for c in a:
    newA+=alph[(alph.index(c)+sA)%26]
for c in b:
    newB+=alph[(alph.index(c)+sB)%26]

rep=''
for c in range(len(newA)):
    rep+=alph[(alph.index(newA[c])+alph.index(newB[c]))%26]
print(rep.upper())