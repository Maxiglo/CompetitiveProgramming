n = int(input())

for i in range(n):
    t1= input()
    t2= input()
    print(t1)
    print(t2)
    for i in range(len(t1)):
        if t1[i]==t2[i]:
            print('.',end="")
            
        else:
            print('*',end="")
        
    print('\n')