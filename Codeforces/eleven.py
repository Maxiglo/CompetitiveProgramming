l=[1,2]

for i in range(2,15):
    s = l[i-2]+l[i-1]
    l.append(s)

rep=''
n = int(input())
for i in range(1,n+1):
    if i in l:
        rep+='O'
    else:
        rep+='o'

print(rep)
        