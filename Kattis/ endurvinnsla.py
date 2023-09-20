city=input()
p=float(input())
n=int(input())
t=0
for _ in range(n):
    if input()=="ekki plast":
        t+=1
print('Neibb' if t/n>p else 'Jebb')