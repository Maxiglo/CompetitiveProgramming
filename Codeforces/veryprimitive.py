a,b,c=map(int,input().split())

if c==0 and a<=b:
    print('Aoki')
elif c==1 and b<=a:
    print('Takahashi')
elif c==0 and a>b:
    print('Takahashi')
elif c==1 and b>a:
    print('Aoki')