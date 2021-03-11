nombre = int(input())
c=0
for chiffre in str(nombre):
    if chiffre=='4' or chiffre=='7':
        c+=1
c2=0
for chiffre in str(c):
    if chiffre =='4' or chiffre =='7':
        c2+=1

if c2==len(str(c)):
    print("YES")
else: print("NO")