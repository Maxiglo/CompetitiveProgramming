n = int(input())
l=[]
l2=[]
tot =0
for i in range(n):
    t,v = map(float,input().split())
    l.append(t)
    l2.append(v)
for i in range(1,len(l)):
    tot += abs(l[i]-l[i-1])*(l2[i]+l2[i-1])/2

print(tot/1000) 