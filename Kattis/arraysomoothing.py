l, k = map(int, input().split())
x = [int(i) for i in input().split()]

s = list(set(x.count(i) for i in x))

for _ in range(k):
    u = s.index(max(s))
    s[u]-=1
print(max(s))
