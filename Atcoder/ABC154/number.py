n=int(input())
l=[2,1]
for i in range(2,n+1):
    x=l[i-1]+l[i-2]
    l.append(x)
print(l[-1])