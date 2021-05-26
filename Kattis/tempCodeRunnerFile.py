n=int(input())

tot=0
for x in range(1,n+1):
    a,b=input().split()
    tot+=x*float(b)
print(tot)