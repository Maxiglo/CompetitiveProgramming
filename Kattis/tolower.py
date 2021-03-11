p,t = map(int,input().split())
c=0
for i in range(p):
    l=[]
    for j in range(t):
        ligne = input()
        l.append(ligne)

    for mot in l:
        if mot[1:].islower():
            low = True
          
        else:
            low= False
            break
 
    if low: c+=1
print(c)
