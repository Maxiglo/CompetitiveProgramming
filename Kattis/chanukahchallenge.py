p = int(input())

for i in range(p):
    a,b = map(int,input().split())
    u = [i+1 for i in range(1,b+1)]
    print(a, sum(u))
  