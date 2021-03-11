import string
n = int(input())
alphabet = string.ascii_lowercase


for i in range(n):
    rep=''
    texte=''
    pasdansalphabet=''
    ligne = input()
    ligne = ligne.lower()
    ligne = ligne.replace(' ','')
    for c in ligne:
        if c.isalnum():
            texte+=c 
    for j in texte:
        if j in alphabet:
            rep+=j
    
    
    if len(set(rep))==26:
        print('pangram')
    
    else:
        for j in alphabet:
            if j not in set(rep):
                pasdansalphabet+=j
        print('missing',pasdansalphabet)