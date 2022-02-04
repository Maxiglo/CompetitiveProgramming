a,b = map(int,input().split())

l =[]
for _ in range(a):
    l.append(input().split())

for i in range(b):
    rep = []
    for j in range(a):
        rep.append(l[j][i])
    print(*rep)