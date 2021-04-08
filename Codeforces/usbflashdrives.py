n = int(input())
m = int(input())

l =[int(input()) for i in range(n)]
l.sort(reverse=True)

c=0
i=0
while m>0:
    m-=l[i]
    i+=1
    c+=1
print(c)