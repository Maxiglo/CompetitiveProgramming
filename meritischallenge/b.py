l = []
with open('b.txt', 'r') as f:
    n = int(f.readline())
    for line in f:
        d, f  = map(int, line.strip().split())
        l.append((d, 'd'))
        l.append((f, 'F'))    
l.sort()

maxc = 0
count = 0

for t, e in l:
    if e == 'd':
        count += 1
    else:
        count -= 1
    maxc = max(maxc, count)
print(maxc)