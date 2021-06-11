import sys
l=[]
for i in range(20):
    l.append(input())


c=0
for ligne in l:
    if ligne.count('#')==9:
        c+=1
if c<4:
    print('NOPE')
    exit()

ind=[]

for i in range(len(l)):
    if l[i].count('#')==9 and len(ind)<4:
        ind.append(i)

tot=0
for i in range(len(ind)-1):
    if ind[i]==ind[i+1]-1:
        tot+=1


if tot<3:
    print('NOPE')
    exit()

s=set()
for i in ind:
    s.add(l[i].index('.'))
if len(s)!=1:
    print('NOPE')
    exit()

pos=l[i].index('.')

ok=False

if ind[-1]+1!=len(l):
    if l[ind[-1]+1][pos]=='#':
        ok=True
if ind[-1]+1==len(l):
    ok=True
ok2=True
for i in range(0,ind[0]):
    if l[i][pos]=='#':
        ok2=False


if ok and ok2:
    print('BOOM',pos+1)

else:
    print('NOPE')


