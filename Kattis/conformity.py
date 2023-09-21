seen=dict()
for _ in range(int(input())):
    x = ' '.join(sorted(map(str,[int(i) for i in input().split()])))
    if x not in seen:
        seen[x]=1
    else:
        seen[x]+=1
t=sorted(seen.values(), reverse=True)[0]
tot=0
for v in sorted(seen.values(), reverse=True):
    if v==t:
        tot+=v
    else:
        break
print(tot)