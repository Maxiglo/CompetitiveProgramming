n = int(input())
a = [int(i) for i in input().split()] 
ans = 0
for i in range(n):
    for j in range(i,n):
        c = a[i:j+1].count(0)
        d = sum(a[:i]+a[j+1:])
        ans = max(ans, c+d)
print(ans)