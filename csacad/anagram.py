d = dict()
for _ in range(int(input())):
    mot = ''.join(sorted(input()))
    if mot not in d:
        d[mot] = 1
    else:
        d[mot] += 1
    
d = sorted(d.items(), key = lambda x : x[1], reverse = True)
print(d[0][1])