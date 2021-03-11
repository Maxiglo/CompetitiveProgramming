n = int(input())
somme=0
for i in range(n):
    p = int(input())
    t = str(p)
    base = t[:-1]
    e = t[-1]
    somme+= int(base)**int(e)
print(somme)