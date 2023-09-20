n, x = map(int, input().split())

tot=0
for _ in range(n):
    tot+=int(input())
if tot<=x:
    print("Jebb")
else:
    print("Neibb")