n = int(input())
l=[float(i) for i in input().split()]
v=0
for x in l:
    v+=x**3
print(v**(1/3))