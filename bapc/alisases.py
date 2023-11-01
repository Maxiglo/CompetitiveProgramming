a,b=map(int,input().split())
l=[]
for _ in range(a):
    l.append(input())
l.sort()

tot=0

def prefix(a,b):
    t=0
    for i,c in enumerate(a):
        if b[i]==c:
            t+=1
        else:
            t+=1
            break
    return t


tot+=prefix(l[0],l[1])
tot+=prefix(l[-1],l[-2])

for i in range(1,a-1):
    tot+=max(prefix(l[i],l[i-1]),prefix(l[i],l[i+1]))
 
print(tot)
