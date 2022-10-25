a,b= map(int, input().split())
l = [int(i) for i in input().split()]

for i in range(b-1,len(l),b):
    print(l[i],end=' ')