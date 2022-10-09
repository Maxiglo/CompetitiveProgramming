tot = 0
rep = 0
for _ in range(int(input())):
    n = int(input())
    tot+=n
    if tot<=0:
        rep = max(abs(tot),rep)
print(rep)