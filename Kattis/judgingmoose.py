x,y = map(int,input().split())
if x == y ==0:
    print("Not a moose")
elif x==y:
    print("Even",x*2)
else:
    print("Odd", 2*max(x,y))