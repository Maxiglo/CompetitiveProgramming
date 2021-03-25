#fct div qui test si les conditions sont respectées 
a,b = map(int,input().split())

def div(num):
    trouve = True
    if len(set(str(num)))!=6:
        trouve= False 
        return trouve
    for i in str(num):
        if i=='0':
            trouve= False
        elif num%int(i)!=0:
            trouve = False
    return trouve
        
c=0
for i in range(a,b+1):
    if div(i):
        c+=1 
print(c)