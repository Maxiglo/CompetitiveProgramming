h,w,x,y = map(int,input().split())

l = []

for i in range(h):
    l.append(input())

c=0
for i in range(y,w):
    if l[x-1][i]=='.':
        c+=1
    else:
        break

for i in range(y-2,-1,-1):
    if l[x-1][i]=='.':
        c+=1
    else:
        break

for i in range(x-2,-1,-1):
    if l[i][y-1]=='.':
        c+=1
    else:
        break

for i in range(x,h):
    if l[i][y-1]==".":
        c+=1
    else:
        break

if l[x-1][y-1]==".":
    c+=1
print(c)

