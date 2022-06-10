s, n = map(int, input().split())

f = []
for _ in range(n):
    x, y = map(int, input().split())    
    f.append([x, y])
f = sorted(f, key = lambda x: x[0])

flag = True 

for v in f:
    if s > v[0]:
        s += v[1]
    else:
        flag = False 
        break 
print('YES' if flag else 'NO')