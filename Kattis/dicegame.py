gunnar = map(int,input().split())
emma = map(int,input().split())

a = sum(gunnar)
b = sum(emma)

if a>b:
    print('Gunnar')
elif a<b:
    print('Emma')
else: print('Tie')
