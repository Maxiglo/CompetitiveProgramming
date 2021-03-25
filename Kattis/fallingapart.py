#problème simple, trier et prendre 1 sur 2

n = int(input())
l= sorted([int(i) for i in input().split()], reverse=True)

alice = 0

for j in range(0,len(l),2):
    alice+=l[j]

print(alice, sum(l)-alice)