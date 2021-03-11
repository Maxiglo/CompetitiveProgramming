n,t= map(int,input().split())
l = list(map(int,input().split()))
somme =0
c =0
for i in range(n):
    c+=l[i]
    if c<=t:
        somme+=1
    if c>= t:
        break
print(somme)