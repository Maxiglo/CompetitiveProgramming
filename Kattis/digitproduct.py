n=input()

while len(str(n))!=1:
    l=[]
    for c in str(n):
        if c!='0':
            l.append(int(c))
    
    t=1
    for i in l:
        t*=i
    n=t 
print(n)