a= input()
b = input()
c= input()
p = True

yep =a+b
for lettre in c:
    if c.count(lettre)!=yep.count(lettre): 
        p= False

if p and len(yep)==len(c):
    print('YES')
else:
    print('NO') 