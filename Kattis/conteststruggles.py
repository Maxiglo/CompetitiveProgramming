n,k= map(int,input().split())
d,s= map(int,input().split())

r = d-((k*s)/n)
rep= (r*n)/(n-k)

if 0<=rep<=100:
    print(rep)
else:
    print('impossible')