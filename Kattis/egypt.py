
while True:
    l=[]
    a,b,c = map(int, input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    
    if a==b==c:
        break
    else:
        if l[2]**2==l[0]**2+l[1]**2:
            print('right')
        else:
            print('wrong')