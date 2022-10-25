x=1 
while True:   
    n = int(input())
    if n==0:
        exit()
    else:
        l = []
        rep1=[]
        rep2=[]
        for i in range(n):
            l.append(input())
        if len(l)%2==0:
            for j in range(0, len(l), 2):
                rep1.append(l[j])
                rep2.append(l[j+1])
        else:            
            for j in range(0, len(l)-1, 2):
                rep1.append(l[j])
                rep2.append(l[j+1])
            rep1.append(l[-1])
        print(f'SET {x}')
        for i in rep1:
            print(i)
        for i in reversed(rep2):
            print(i)
        x+=1