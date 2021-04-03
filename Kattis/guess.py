# Problème : Guess The Number - Difficulté 3.0 (2.9 quand je l'ai fait) 

# Description: On doit trouver un nombre entre 1 et 1000 en maximum 10 étapes.

# Subtilités: Aucune, le problème est assez simple, c'est juste de l'implémentation. 
# Il faut juste faire attention à faire une division entière car le résultat cherché est un entier.

# Méthode: On boucle tant que la réponse n'a pas été trouvée. On commence par prendre 
# l'intervalle 1-1000 avec 500 comme milieu, si le nombre est inférieur à 500, 
# la borne supérieure devient le milieu-1, si le nombre est supérieur à 500 alors la borne 
# inférieure devient le milieu + 1.  
# On peut calculer le milieu en faisant simplement une moyenne arithmétique
# et comparer le milieu avec le nombre voulu. Tant que le nombre cherché n'est pas trouvé, 
# on redéfinit les bornes et on affine la recherche. 

#initialisation des bornes
inf = 1
sup = 1000
mid = (inf + sup)//2
print(mid)

while True:
    try:
        #lecture de l'entrée qui nous dit si ce qu'on affiche est correct, trop grand ou trop petit
        rep = input()
        if rep=="correct":
            break
        #on redéfinit les bornes en fonction de l'entrée
        elif rep =="lower":
            sup = mid-1
        elif rep=="higher":
            inf = mid +1
        #calcul du milieu 
        mid = (inf + sup)//2
        print(mid)
    except EOFError:
        break