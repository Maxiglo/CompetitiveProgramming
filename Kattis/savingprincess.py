#probleme nul
n,y = map(int,input().split())
s=set()
for i in range(y):
    s.add(int(input()))

for j in range(n):
    if j not in s:
        print(j)
print(f'Mario got {len(s)} of the dangerous obstacles.')