n = int(input())
a = [int(i) for i in input().split()]


r=[]
for j in a:
    c=0
    for i in range(len(a)):
        if a[i]>=j:
            c+=1
    r.append(c)

l=[]
for num in r:
    if r.count(num)>1:
        l.append(num)
for k in range(len(r)):
    if r[k] in l:
        r[k]-=l.count(r[k])-1
print(*r)
