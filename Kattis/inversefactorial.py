# Problème- Inverse Factorial - Difficulté: 5.3

# Description: On connait la valeur de n! et on veut trouver n
# Exemple: si l'entrée vaut 120, alors n! = 120 donc n = 5 car 5! = 120

# Subilités: Problème super sympa, on utilise ce qu'on a vu en cours pour calculer la longueur d'une factorielle 
# mais dans l'autre sens. 
# Comme on connait la valeur de n!, on connait aussi la longueur de n!. On sait que chaque factorielle 
# aura une longueur différente donc si on connait la longueur d'une factorielle, on peut itérer 
# dans une boucle en incrémentant une variable ici appelée fact_len et tant que cette variable 
# n'a pas la même longueur que la longueur de la factorialle qu'on cherche, on incrémente.
# Pour calculer la longueur d'une factorielle, on utilise l'astuce vue en cours avec le log en base 10.

# Méthode: Itérer tant qu'on a pas la longueur voulue en incrémentant un compteur appelé i. Lorsque la 
# longueur correspond à la longueur recherchée, alors on connait n.  

import sys,math


def main():
    #lecture de l'entrée
    n = sys.stdin.readline().strip()
    #longueur de la factorielle
    length = len(n)
    #on hardcode les valeurs du début car au début, 5! à la même longueur que 6! donc ça pose problème
    #par la suite, la longueur s'incrémente toujours donc aucun problème
    facts_set = {'1':1, '2':2, '6':3, '24':4, '120':5, '720':6}
    if n in facts_set:
        print (facts_set[n])
        return

    #initialisation de la longueur et de i
    fact_len = 0.0
    i = 0
    #tant que la longueur est différente de la longueur de la factorielle, on incrémente
    while int(fact_len)+1 != length:
        i += 1
        fact_len += math.log(i,10)
    print (i)

main()