n=int(input())
l=[int(i) for i in input().split()]

somme=sum(l)
r=set()
for i in l:
    r.add(somme-i)
print(len(r))
print(*sorted(r))