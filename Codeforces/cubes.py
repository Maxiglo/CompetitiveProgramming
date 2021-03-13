n = int(input())

c=0
i=0
bloc = 0
while n>0:
    i+=1
    bloc = bloc +i 
    if n <bloc:
        break
    else:
        n=n-bloc
        c+=1
print(c)