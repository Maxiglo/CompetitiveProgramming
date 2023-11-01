t,s=map(int, input().split())
times=sorted([int(i) for i in input().split()])
total=t*60
r=0
for i in times:
    if total-i>=0:
        total-=i
        r+=i
    else:
        break
print(r)

