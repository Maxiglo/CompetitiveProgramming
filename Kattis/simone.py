n,k=map(int,input().split())
x=list(map(int,input().split()))
occ=[(i,x.count(i)) for i in range(1,k+1)]
occ.sort(key=lambda x: x[1])
temp = occ[0][1]
rep=[]
for c in occ:
    if c[1]==temp:
        rep.append(c[0])
print(len(rep))
print(*rep)
