a,b,c=map(int,input().split())

cp=0 
for i in range(a,b+1):
    if i%c==0:
        cp+=1
print(cp)