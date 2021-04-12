n = int(input())
l1=[]
l2=[]
for i in range(n):
    a,b= map(int,input().split())
    l1.append(a)
    l2.append(b)

y =sorted(l1)
z= sorted(l2)


if l1.index(y[0])==l2.index(z[0]):
    if y[0]+z[0]<max(y[0],z[1]) and y[0]+z[0]<max(y[1],z[0]):
        print(y[0]+z[0])
    else:
        if y[0]+z[1]<y[1]+z[0]:
            print(max(y[0],z[1]))
        else:
            print(max(y[1],z[0]))

else:
    print(max(y[0],z[0]))
    
