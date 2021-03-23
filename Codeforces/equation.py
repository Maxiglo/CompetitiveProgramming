n = int(input())
def composite(nombre):
    for i in range(2,nombre):
        if nombre%i==0:
            return True 



i= n+1
while True:
    if composite(i) and composite(i-n):
        print(i,i-n)
        break
    i+=1
