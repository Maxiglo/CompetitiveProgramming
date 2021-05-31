n=int(input())
if n %2!=0:
    print('still running')
    exit()
l=[]
for _ in range(n):
    l.append(int(input()))
tot=0
for i in range(0,len(l)-1,2):
    tot+=l[i+1]-l[i]
print(tot)