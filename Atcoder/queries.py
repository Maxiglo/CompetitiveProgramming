from collections import defaultdict
 
N, Q = map(int, input().split())
A = list(map(int, input().split()))

ind = defaultdict(list)
for i, a in enumerate(A, 1):
    ind[a].append(i)
for i in range(Q):
    x, k = map(int, input().split())
    if len(ind[x]) >= k:
        print(ind[x][k - 1])
    else:
        print(-1)