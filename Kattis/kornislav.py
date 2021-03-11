a,b,c,d = map(int,input().split())
a2 = min(a,b,c,d)
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
a3 = sorted(l)
aire = a2*a3[2]
print(aire)