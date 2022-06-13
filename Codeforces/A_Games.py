ha = []
aa = []
n = int(input())
for _ in range(n):
    h, a = map(int, input().split())
    ha.append(h)
    aa.append(a)
c = 0
for i in range(n):
    for j in range(n):
        if ha[i] == aa[j]:
            c+=1
print(c)