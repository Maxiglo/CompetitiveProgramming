a,b = map(int,input().split())
l= [int(i) for i in input().split()]

c=0
while len(l)>0:
    premier = l[0]
    last= l[-1]
    if premier<=b:
        c+=1
        del l[0]
    elif last<=b:
        c+=1
        del l[-1]
    else:
        break

print(c)