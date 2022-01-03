n= int(input())

for _ in range(n):
    x = int(input())
    i=1
    s=set()
    while i**2<=x:
        s.add(i**2)
        i+=1
         
    j=1

    while j**3<=x:
        s.add(j**3)
        j+=1
    print(len(s))