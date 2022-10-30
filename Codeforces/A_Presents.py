n = int(input())
x = [int(i) for i in input().split()]

rep = [0 for _ in range(n)]

for i in range(len(x)):
    rep[x[i]-1]=i+1
print(*rep)
