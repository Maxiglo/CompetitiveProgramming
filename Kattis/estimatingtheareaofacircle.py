import math
while True:
    r,m,c = map(float,input().split())
    if r==0:
        break
    vaire = math.pi * (r**2)
    cotecarre = 2*r
    app = (c/m)* (cotecarre**2)

    print(vaire, app) 