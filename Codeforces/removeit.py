n,x=map(int,input().split())
l=[int(i) for i in input().split()]
r=[]
for c in l:
    if c!=x:
        r.append(c)
print(*r)