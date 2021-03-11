import sys

sommemax = 0
for i in range(5):
    somme = 0
    notes = list(map(int,sys.stdin.readline().split()))
    for j in notes: 
        somme+=j
        if somme> sommemax:
            sommemax = somme
            indice = i+1

print(indice, sommemax)