a,b=map(int,input().split())

ans=1
for j in range(1,min(a,b)+1):
    ans*=j
print(ans)