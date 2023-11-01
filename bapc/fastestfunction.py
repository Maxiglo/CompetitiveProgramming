n,k=map(int,input().split())
l=[int(i) for i in input().split()]

h=0
s=sorted(l)
for heure in range(1000):
    for i in range(len(l)):
        start=i
        end=i+k
        l[start:end]=sorted(l[start:end])
    h+=1
    if l==s:
        break
print(h)