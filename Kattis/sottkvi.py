n,k,d=map(int,input().split())
tot=0
for _ in range(n):
    f = int(input())
    if k+d-f>=14:
        tot+=1
print(tot) 