# Problème- Inverse Factorial - Difficulté: 5.3

# Description: On connait la valeur de n! et on veut retrouver n
# Exemple: si l'entrée vaut 120, cela veut dire que n! = 120 donc n = 5 car 5! = 120

# Subilités: La solution naîve ne fonctionne pas ici, étant donné que n! peut valoir jusqu'à 10^6 et que le temps limite est de 1 seconde. 
# On va donc utiliser ce qu'on a vu en cours pour calculer la longueur d'une factorielle 
# mais dans l'autre sens. 

# n= 0  fact= 1             longueur= 1
# n= 1  fact= 1             longueur= 1
# n= 2  fact= 2             longueur= 1
# n= 3  fact= 6             longueur= 1
# n= 4  fact= 24            longueur= 2
# n= 5  fact= 120           longueur= 3
# n= 6  fact= 720           longueur= 3
# n= 7  fact= 5040          longueur= 4
# n= 8  fact= 40320         longueur= 5
# n= 9  fact= 362880        longueur= 6
# n= 10 fact= 3628800       longueur= 7
# n= 11 fact= 39916800      longueur= 8
# n= 12 fact= 479001600     longueur= 9
# n= 13 fact= 6227020800    longueur= 10
# n= 14 fact= 87178291200   longueur= 11
# n= 15 fact= 1307674368000 longueur= 13
# On remarque que lorsque n>6, chaque factorielle peut être identifiée par sa longueur (son nombre de chiffres)
# Si n<7 alors ce n'est pas possible d'identifier la factorielle par sa longueur car comme on le voit, plusieurs 
# factorielles sont de longueur 1 etc


# Comme on connait la valeur de n!, on connait aussi la longueur de n!. On sait que chaque factorielle 
# aura une longueur différente (quand n>6) donc si on connait la longueur d'une factorielle, on peut itérer 
# dans une boucle en incrémentant une variable ici appelée fact_len et tant que cette variable 
# n'a pas la même longueur que la longueur de la factorialle qu'on cherche, on incrémente.
# Pour calculer la longueur d'une factorielle, on utilise le log en base 10.

# Chaque étape de la méthode va coûter O(1) et on sait que la réponse sera trouvée en maximum 3*10^5 étapes, il nous
# reste simplement à traiter les cas où n<7 car on ne peut pas identifier les factorielles par leur longueur 
# étant donné que, comme on le remarque dans l'exemple au-dessus, 5!=120 et 6!=720 ont la même longueur

# Méthode: Itérer tant qu'on a pas la longueur voulue en incrémentant un compteur appelé i. Lorsque la 
# longueur correspond à la longueur recherchée, alors on connait n.  

import sys,math

# Pas très utile dans notre cas car l'entrée est seulement un seul nombre mais dans un problème avec beaucoup
# d'entrées, utiliser sys.stdin.readline est environ 8 fois plus rapide et le définir comme ça au début nous facilite 
# la vie car beaucoup plus rapide de taper input que sys.stdin.readline
input = sys.stdin.readline

def main():
    # lecture de l'entrée
    n = input().strip()

    # longueur de la factorielle
    length = len(n)

    # On hardcode les cas particuliers lorsque n<7 car au début, 5! à la même longueur que 6! donc ça pose problème
    # par la suite, la longueur s'incrémente toujours donc aucun problème
    facts_set = {'1':1, '2':2, '6':3, '24':4, '120':5, '720':6}
    
    # On check si la valeur en entrée ne fait pas partie des cas particuliers, si c'est le cas, on peut directement afficher n
    if n in facts_set:
        print (facts_set[n])
        return

    # Initialisation de la longueur à 0 et de i
    fact_len = 0.0
    i = 0
    #tant que la longueur est différente de la longueur de la factorielle que l'on cherche, on incrémente
    while int(fact_len)+1 != length:
        i += 1
        fact_len += math.log(i,10)
    # Quand la longueur correspond à la valeur recherchée, c'est qu'on a trouvé n -> on affiche i
    print (i)

main()