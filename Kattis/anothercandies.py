n = int(input())

for i in range(n):
    input()
    nombre= int(input())
    somme=0
    for j in range(nombre):
        sucette = int(input())
        somme+=sucette
    reste= somme%nombre
    if reste==0:
        print('YES')
    else: print('NO')