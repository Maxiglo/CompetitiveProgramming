from sys import stdin, stdout
input = stdin.readline
 
 
def start(x,n):
    if x in done:
        return done[x]
    ans=float('inf')
    if len(str(x))>n:
        done[x]=ans
        return ans
    if len(str(x))==n:
        done[x]=0
        return 0
    for i in set(str(x)):
        if int(i)>1:
            ans=min(ans,start(x*int(i), n,)+1)
    done[x]=ans
    return ans
 
t = 1
for _ in range(t):
    done={}
    n,x=map(int,input().split())
    ans=start(x,n)
    if ans==float('inf'):
        ans=-1
    print(ans)
