n = int(input())

l=[int(i) for i in input().split()]
l.sort()
while len(l)>1:
    if len(l)==2:
        del l[-1]
    
    else:
        del l[-1]
        del l[0]
print(l[0])