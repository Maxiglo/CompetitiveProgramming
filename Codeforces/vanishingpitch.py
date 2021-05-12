v,t,s,d=map(int,input().split())
temps=d/v

if temps<t or temps>s:
    print('Yes')
else:
    print('No')