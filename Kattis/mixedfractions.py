import math
while True:
    a,b = map(int,input().split())

    if a==b==0:
        break
    else:
        print(math.floor(a/b), a%b,'/',b)