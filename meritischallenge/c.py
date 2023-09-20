import random

l = []


with open('c.txt', 'r') as f:
    n = int(f.readline())
    for i, line in enumerate(f):
        d, f, r = map(int, line.strip().split())
        l.append((d,f,r))


# Fonction pour calculer la somme des revenus des missions sélectionnées
def somme_revenus(missions, selection):
    return sum(missions[i][2] for i in selection)

# Fonction pour générer une solution initiale aléatoire
def solution_initiale(missions):
    n = len(missions)
    selection = []
    while somme_revenus(missions, selection) == 0:
        selection = random.sample(range(n), random.randint(1, n))
    return selection

# Fonction pour améliorer la solution en effectuant une modification locale
def modification_locale(missions, selection):
    n = len(missions)
    best_selection = selection
    best_revenus = somme_revenus(missions, selection)
    for i in range(n):
        for j in range(i+1, n):
            nouvelle_selection = selection[:i] + selection[j:j+1] + selection[i+1:j] + selection[i:i+1] + selection[j+1:]
            nouveaux_revenus = somme_revenus(missions, nouvelle_selection)
            if nouveaux_revenus > best_revenus:
                best_selection = nouvelle_selection
                best_revenus = nouveaux_revenus
    return best_selection

# Fonction pour exécuter l'algorithme de recherche locale
def recherche_locale(missions):
    n = len(missions)
    selection = solution_initiale(missions)
    iterations = 1000
    while iterations > 0:
        nouvelle_selection = modification_locale(missions, selection)
        nouveaux_revenus = somme_revenus(missions, nouvelle_selection)
        if nouveaux_revenus > somme_revenus(missions, selection):
            selection = nouvelle_selection
        iterations -= 1
    return [i+1 for i in selection]


selection = recherche_locale(l)
print("Indices des missions sélectionnées :", selection)
print("Revenus totaux :", somme_revenus(l, selection))