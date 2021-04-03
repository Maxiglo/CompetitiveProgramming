# Problème: Ones - Difficulté 4.3

# Description: On nous donne un nombre n entre 1 et 100 000, on sait qu'un multiple de ce nombre est égal à une séquence de 1
# et on veut savoir le nombre minimal de 1 pour écrire ce mulitple de n.
# Par exemple avec 3, le plus petit mulitple de 3 qui est une séquence de 1 vaut 111 de longueur 3 donc on doit afficher 3.  

# Subtilités: La solution naïve ne fonctionne forcément pas avec des entrées qui peuvent atteindre 100 000.
# L'astuce ici est d'utiliser le modulo pour simplifier les opérations.

# Méthode: On boucle tant que le nombre n'est pas un mulitple de n. On calcule le modulo du total et on fait l'opération *10 +1.
# On initialise le total à 1, on va donc aller à 11 (1*10+1=11), 111 1111...
# On travaille sur le modulo du total avec le nombre d'entrée car on veut qu'il soit égal à 0 (car on cherche un multiple de n).
# Pour chaque étape supplémentaire, on incrémente le compteur c de 1 car cela prendra un chiffre de plus (on passe de 11 -> 111-> 1111->..)


import sys
def solve(num):
    #initialisation du compteur et du total qu'on calcule
    c=1
    tot=1
    #on boucle tant qu'on a pas un multiple
    while(tot%num !=0):
        tot= tot%num
        tot= tot*10+1
        c+=1
    return c

def main():
    #lecture de l'entrée et appel de la fonction pour chaque entrée
    for n in sys.stdin:
        print(solve(int(n)))
   
main()