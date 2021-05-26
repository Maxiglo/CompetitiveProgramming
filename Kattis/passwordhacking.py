n=int(input())

tot=0
l=[]
for x in range(1,n+1):
    a,b=input().split()
    l.append(float(b))
l.sort(reverse=True)
t=1
for c in l:
    tot+=t*c
    t+=1
print(tot)