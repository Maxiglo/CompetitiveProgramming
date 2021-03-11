a,b,c = map(int,input().split())

result = a*3+b*2+c*1

l=[]
l2=[]
if result>=8:
    l.append('Province')
if result>=5:
    l.append('Duchy')
if result>=2:
    l.append('Estate')
if result>=6:
    l2.append('Gold')
if result>=3:
    l2.append('Silver')
if result>=0:
    l2.append('Copper')

if len(l)>0:
    print(l[0],'or',l2[0])
else:
    print(l2[0])