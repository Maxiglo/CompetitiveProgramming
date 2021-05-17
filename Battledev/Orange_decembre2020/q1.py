n=int(input())
s=set()
for i in range(n):
    taille=int(input())
    if taille<=250:
        s.add(taille)
print(sorted(list(s))[-1])