n = int(input())
target = [0]
under = []
A = []
B = []
res = [1]

for _ in range(n-1):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for _ in range(9):
    for i in range(len(B)):
        if B[i] in target:
            under.append(A[i])

    res.append(len(under))
    target = under
    under = []
print(*res)