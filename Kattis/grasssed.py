c = float(input())
l = int(input())
somme = 0
for i in range(l):
    w,l = map(float,input().split())
    somme += w*l*c
print(somme)