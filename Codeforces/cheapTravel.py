a,b,c,d = map(int,input().split())

m = 10**10

for i in range(1001):
    for j in range(1001):
        if i*b + j >=a:
            m = min(m,j*c+i*d)
print(m)