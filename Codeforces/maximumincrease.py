n = int(input())
l = [int(i) for i in input().split()]
l.append(0) #solution barbare
rep=0
best=0
for num in range(len(l)-1):
    if l[num+1]>l[num]:
        rep+=1
    else:
        if rep>best:
            best=rep
        rep=0
      
print(best+1)    