n = int(input())
if n%2!=0 or n==0:
    print('impossible')
    exit()

l=[]
u=[]
for _ in range(n):
    a,b = map(int, input().split()) 
    l.append(a)
    u.append(b)

z=list(zip(l,u))

m1=int(2*(sum(l)/len(l)))
m2=int(2*(sum(u)/len(u)))

for (a,b) in z[::len(z)//2]:
    if z.count((a,b)) != z.count((m1-a,m2-b)):
        print('impossible')
        exit()
        
print('possible')


## deuxième idée 
n = int(input())
if n%2!=0 or n==0:
    print('impossible')
    exit()

l=[]
u=[]
for _ in range(n):
    a,b = map(int, input().split()) 
    l.append(a)
    u.append(b)

z=sorted(list(zip(l,u)), key=lambda x:x[0])
z=sorted(z, key=lambda x:x[1])


temp1=z[0][0]+z[len(z)-1][0]
temp2=z[0][1]+z[len(z)-1][1]

for (a,b) in z[::len(z)//2]: 
    if z.count((a,b)) != z.count((temp1-a,temp2-b)):
        print('impossible')
        exit()
        
print('possible')