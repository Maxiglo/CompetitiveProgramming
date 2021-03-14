n = int(input())

for i in range(n):
    c=0
    l = int(input())
    nombres =[int(i) for i in input().split()]
    c= nombres.count(0)
    for num in range(len(nombres)):
        if nombres[num]==0:
            nombres[num]+=1
      
    if sum(nombres)==0:
        c+=1
    print(c)
