s,v1,v2,t1,t2= map(int,input().split())
temps1 = v1*s+t1*2
temps2= v2*s+t2*2

if temps1<temps2:
    print('First')
elif temps2<temps1:
    print('Second')
else:
    print('Friendship')