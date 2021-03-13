k,n,w = map(int,input().split())
prix= 0
for i in range(1,w+1):
    prix+=i*k
sold= prix-n
if sold>0:
    print(sold)
else:
    print(0)