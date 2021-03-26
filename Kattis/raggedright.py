#programme super basique, seule utilité = CTRL Z pour simuler une eof error sur windows
l=[]
tot=0
lmax=0
while True:
    try:
        ligne = input()
        if len(ligne)>lmax:
            lmax= len(ligne)
        l.append(ligne)
    
    except EOFError:
        break


for i in range(len(l)-1):
    tot+=(lmax-len(l[i]))**2
print(tot)