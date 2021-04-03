# Problème : Almost Perfect - Difficulté: 3.3

# Description: Un entier n est considéré parfait si la somme de ses diviseurs propres est égale à n. 
# On cherche donc à savoir pour différents entiers s'ils sont parfaits, presque parfaits (écart de maximum 2 avec n) 
# ou bien non parfaits.

# Subtilités: L'idée est assez simple, il suffit de trouver les diviseurs d'un entier, de les sommer et de les comparer 
# avec l'entier, mais on ne peut pas utiliser une méthode naïve pour trouver tous les diviseurs de l'entier.
# Si on fait la méthode naïve en O(n) pour trouver les diviseurs de N, on a un TLE.
# On peut donc utiliser une méthode en O(sqrt(N)) qui fonctionne bien dans notre cas car l'ordre n'a pas d'importance, on ne 
# doit donc pas refaire un tri par la suite.

# Méthode:  On calcule les diviseurs de n en allant jusqu'à la racine carrée de n. On ajoute dans un set i et son complémentaire.
# Ici on utilise un set pour éviter d'avoir des doublons. 
# Par exemple pour n=10, on ajoutera 2 et 10/2 donc 5 dans le set. Cela permet d'itérer seulement jusqu'à la racine (similaire aux méthodes
# vues en cours avec les nombres premiers)
# Lorsqu'on connait les diviseurs de n, on calcule juste la somme et on la comparer à n. En fonction de la comparaison, 
# on print perfect si la somme des diviseurs = n, almost perfect si la somme diffère de maximum 2 par rapport à n et not perfect sinon.


import math
#O(srqt(n)) pour la recherche des diviseurs, la solution naîve en O(n) ne passe pas les tests cases (TLE)
#ici l'ordre n'a pas d'importance, pas besoin de refaire un tri par la suite, on prend juste la somme donc
#ce n'est pas un problème d'avoir les diviseurs non ordonnés
def diviseurs(num):
    # on met 1 dans le set ainsi on évite d'avoir n dans le set et de devoir le retirer après
    # permet de faire une opération en moins, on passe de 0.12s à 0.11s 
    s= {1}
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num%i==0:
            s.add(i)
            s.add(num/i)
    return s


def main():
    while True:
        try:
            #lecture de l'entrée
            n =int(input())
            #conditions
            if sum(diviseurs(n))==n:
                print(n,'perfect')
            elif n-2<=sum(diviseurs(n))<=n+2:
                print(n,'almost perfect')
            else:
                print(n,'not perfect')
        except EOFError:
            break
main()

# Nb: Je sais qu'il n'est pas recommandé d'utiliser while True dans un programme mais quand on ne connait pas la 
# dimension de l'entrée, je trouve que ça fonctionne bien surtout qu'on peut générer facilement une EOF sur windows 
# avec CTRL Z enter donc ça ne pose pas de problème lors des tests.