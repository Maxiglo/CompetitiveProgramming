n = int(input())
noms=[]

d={}
for i in range(n):
    nom,prenom,cours= input().split()
    yep = nom + prenom + cours
    
    if yep not in noms and cours not in d.keys():
        d[cours]=1
    elif nom+prenom+cours not in noms and cours in d.keys():
        d[cours]+=1
    noms.append(yep)

sortedd= dict(sorted(d.items(), key= lambda x:x[0]))

for cle,valeur in sortedd.items():
    print(cle,valeur)