n = int(input())
l= [int(i) for i in input().split()]


maximum =0
minimum = 10000
c=-2
for nombre in  l:
    if nombre > maximum:
        maximum=nombre
        c+=1
    if nombre<minimum:
        minimum=nombre
        c+=1

if c ==-1:
    print(0)
elif c==0 and len(l)>1 and len(set(l))>1:
    print(1)
else:
    print(c)