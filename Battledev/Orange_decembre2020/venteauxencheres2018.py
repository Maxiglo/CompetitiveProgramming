n=int(input())
prix=int(input())
ok=0
pmax=0
for i in range(n):
    p,e=input().split()
    p=int(p)
    if p >prix and p >pmax:
        ok=1
        pmax=p
        nom=e
        

if ok:print(nom)
else:print('KO')