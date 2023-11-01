from functools import reduce 

for _ in range(int(input())):
    n = int(input())
    l = sorted([int(i) for i in input().split()])
    l[0]+=1
    product=reduce(lambda x,y:x*y,l)
    print(product)