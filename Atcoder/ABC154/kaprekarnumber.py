def solve(num):
    nums=list(num)
    g1=''.join(sorted(nums, reverse=True))
    g2=''.join(sorted(nums))
    f=int(g1)-int(g2)
    return f 

n,k=map(str,input().split())

for i in range(int(k)):
    n=solve(str(n))
print(n)