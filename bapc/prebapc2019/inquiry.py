n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))


a=sum(x**2 for x in l)
b=0
rep=0

for val in l[::-1]:
    a-=val**2
    b+=val
    rep=max(rep,a*b)
print(rep)