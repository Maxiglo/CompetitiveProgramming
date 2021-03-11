a = int(input())
trouve= False
for i in range(a):
    c= 0
    d=0

    b = int(input())
    nom= input()
    for j in range(1,b+1):
        t= input()
        if t=='pea soup':
            c+=1
        if t=='pancakes':
            d+=1
    if c>=1 and d>=1:
        trouve= True
        resto = nom
        break
    
if trouve:
    print(resto)
else: print('Anywhere is fine I guess')    
