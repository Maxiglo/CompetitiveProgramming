n = int(input())

for i in range(n):
    a,b,c = map(int,input().split())
    print((max(a,max(b,c)+1))-a,max(b,max(c,a)+1)-b,max(c,max(a,b)+1)-c)
    