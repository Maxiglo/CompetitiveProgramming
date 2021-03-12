a,b = map(int,input().split())

c1=0
c2=0
c3=0
possibilite=[1,2,3,4,5,6]

for i in possibilite:
    if abs(a-i)<abs(b-i):
        c1+=1
    elif abs(a-i)>abs(b-i):
        c2+=1
    else:
        c3+=1
print(c1,c3,c2)