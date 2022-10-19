n = int(input())

square = [int(i)**2 for i in range(2,n)] 

def test(x, square):
    for s in square:
        if x%s==0:
            return False 
    return True 
            

for i in range(2,1000):
    x=n*i
    if test(x, square):
        print(i)
        exit()


    

