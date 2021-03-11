from collections import Counter
lx=[]
ly=[]
for i in range(3):
    x,y = map(int, input().split())
    lx.append(x)
    ly.append(y)
    
    a = Counter(lx)
    b = Counter(ly)
    a = dict(sorted(a.items(), key=lambda item: item[1]))
    b = dict(sorted(b.items(), key=lambda item: item[1]))

r =list(a.keys())[0]
s =list(b.keys())[0]
print(r,s)