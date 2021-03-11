n = int(input())
somme =2
for i in range(n):
    somme+= somme-1
print(somme**2)