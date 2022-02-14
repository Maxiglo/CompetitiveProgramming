n, m = map(int, input().split())
suc = [i+1 for i in range(n)]
p = [0 for i in range(n)]
diff = []
for _ in range(m):
    a,b =map(int,input().split())
    p[a-1] += 1
    p[b-1] += 1

z = zip(suc,p)

for a,b in z:
    diff.append(b-a)

print(*diff)
