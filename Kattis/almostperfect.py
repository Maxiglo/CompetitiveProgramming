import math
#O(srqt(n)) pour la recherche des diviseurs, la solution naîve en O(n) ne passe pas les tests cases (TLE)
#ici l'ordre n'a pas d'importance, pas besoin de refaire un tri par la suite, on prend juste la somme donc
#ce n'est pas un problème d'avoir les diviseurs non ordonnés
def diviseurs(num):
    l=[]
    for i in range(1, math.ceil(math.sqrt(num))+1):
        if num%i==0:
            if(n/i==i):
                l.append(i)
            else:
                l.append(i)
                l.append(n/i)
    l.remove(n)
    s = set(l)
    return s



while True:
    try:
        n =int(input())
        if sum(diviseurs(n))==n:
            print(n,'perfect')
        elif n-2<=sum(diviseurs(n))<=n+2:
            print(n,'almost perfect')
        else:
            print(n,'not perfect')
    except EOFError:
        break