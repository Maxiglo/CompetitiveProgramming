for j in range(5):
    ligne = [int(i) for i in input().split()]
    for k in range(len(ligne)): #plus intelligent d'utiliser .index pour avoir l'index de 1 dans la ligne 
        if ligne[k] ==1:
            x = j
            y=k

dist= abs(2-x)+abs(2-y) 
print(dist)