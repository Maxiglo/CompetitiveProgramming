n = int(input())

c =0
for i in range(n):
    couleur = input().lower()
    if 'pink' in couleur or 'rose' in couleur :
        c+=1
    

if c==0:
    print("I must watch Star Wars with my daughter")
else : print(c)

