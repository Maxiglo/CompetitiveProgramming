l = []
for _ in range(int(input())):
    nom, score,a = input().split()
    l.append([nom,score,a])

l = sorted(l,key = lambda x: int(x[1]), reverse=True)


rep = []
annif = []
for val in l:
    if val[2] not in annif:
        rep.append(val[0])
        annif.append(val[2])
print(len(rep))
rep.sort()
for v in rep:
    print(v)




