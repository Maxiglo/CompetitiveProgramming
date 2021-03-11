n,h,v = map(int,input().split())

taillemax = 0
if h*v*4> taillemax:
    taillemax= h*v*4
if (n-h)*v*4>taillemax:
    taillemax = (n-h)*v*4
if (n-v)*h*4> taillemax:
    taillemax = (n-v)*h*4
if (n-v)*(n-h)*4>taillemax:
    taillemax=(n-v)*(n-h)*4
print(taillemax)
