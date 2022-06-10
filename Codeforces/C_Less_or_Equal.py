n, k = map(int, input().split())
a = sorted(map(int, input().split()))
if k == 0:
    if a[0] == 1:
        ans = -1
    else:
        ans = 1
elif k == n:
    ans = a[-1]
elif a[k] != a[k-1]:
    ans = a[k]-1
else:
    ans = -1
print(str(ans)+"\n")