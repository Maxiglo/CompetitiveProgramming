n, l = map(int, input().split())
a = sorted([int(i) for i in input().split()])
b = 0
for i in range(len(a)-1):
    b = max(b, (a[i]-a[i-1])/2, (a[i+1]-a[i])/2)
b = max(b, a[0]-0, l-a[-1])
print(b)





