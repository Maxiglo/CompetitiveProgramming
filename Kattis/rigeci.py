a = [0,1]
b= [1,1]
n = int(input())

for i in range(n):
    a.append(a[-1]+a[-2])
    b.append(b[-1]+b[-2])
print(a[n-1],b[n-1])