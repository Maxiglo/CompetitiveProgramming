a = int(input())
l=[]
for i in range(a):
    a,b= map(int,input().split())

    for i in range(a,b+1):
        l.append(i)

print(len(set(l))) 