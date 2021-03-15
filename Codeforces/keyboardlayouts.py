s = input()
sup= s.upper()
premier= list(s+sup)

second = input()
secondup= second.upper()
deuxieme = list(second+secondup)

mot= input()
rep=''

for lettre in mot:
    if lettre in deuxieme:
        pos = premier.index(lettre)
        rep+=deuxieme[pos]
    else:
        rep+=lettre
print(rep)