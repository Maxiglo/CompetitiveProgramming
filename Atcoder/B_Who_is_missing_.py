import collections
n = int(input())
l = [int(i) for i in input().split()]
c = collections.Counter(l)
for k,v in c.items():
    if v < 4:
        print(k)
        exit()
