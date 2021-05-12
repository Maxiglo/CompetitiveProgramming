n = int(input())
a = list(map(int, input().split()))
 
mp = {}
ans = 0
for x in a:
    if x%200 in mp:
        ans += mp[x%200]
    else:
        mp[x%200] = 0
    mp[x%200] += 1
print(ans)