import math
n=int(input())
 
s=input().split()
 
ans=s.count('4')
x=s.count('1')
i=s.count('3')
ans+=i
x-=i
y=s.count('2')
ans+=(y//2)+y%2
 
if(y%2==1):
    x-=2
if(x>0):
    ans+=math.ceil(x/4)
    
 
print(ans)

