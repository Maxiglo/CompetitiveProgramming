n,k = map(int,input().split())
x = 0
if n%2 == 0:
    if k <= n//2:
        x = 1 + (k-1)*2
 
    elif k > n//2:
        k = k-(n//2)
        x = 2 + (k-1)*2
 
else:
    if  k <= (int(n/2)+1):
        x = 1 + (k - 1) * 2
 
    elif k > (int(n/2) + 1):
        k = k-(n//2)-1
        x = 2 + (k-1)*2
print(x)