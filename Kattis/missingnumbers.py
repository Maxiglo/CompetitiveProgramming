n = int(input())
l=[]
for i in range(n):
    t = int(input())
    l.append(t)
l2=[]
for i in range(1,l[-1]):
    if i not in l:
        l2.append(i)

if len(l2)==0:
    print('good job')
else:
    for i in l2:
        print(i)