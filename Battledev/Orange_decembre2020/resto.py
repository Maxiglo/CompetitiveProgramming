from math import ceil

prix = int(input())
n = int(input())
nb_personnes = [int(input()) for i in range(n)]

def note(prix, k):
    x = prix*k
    if k >= 10:
        x *= 0.7
    elif k >= 6:
        x *= 0.8
    elif k >= 4:
        x *= 0.9
    return x

print(ceil(sum(note(prix, k) for k in nb_personnes)))