mot = input()
l=0
u=0
for lettre in mot:
    if lettre.islower():
        l+=1
    else:
        u+=1
if u>l:
    print(mot.upper())
else:
    print(mot.lower())
