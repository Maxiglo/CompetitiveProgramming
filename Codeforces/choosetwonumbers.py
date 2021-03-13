n = int(input())
a = [int(i) for i in input().split()]
n2= int(input())
b=  [int(j) for j in input().split()]

l=[]

for x in a:
    for y in b:
        if x+y not in a and x+y not in b:
            l.append(x)
            l.append(y)
            break
print(l[0],l[1]) 