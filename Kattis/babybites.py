n = int(input())
l = [i for i in input().split()]
ok=True
for j in range(len(l)):
    if l[j]!=str(j+1) and l[j]!='mumble':
        ok=False
        
if ok:print('makes sense')
else:print('something is fishy')