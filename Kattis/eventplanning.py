n,b,h,w=map(int,input().split())
minprix=1000000000
prix=100000000
for _ in range(h):
    p=int(input())
    a=[int(i) for i in input().split()]
    for c in a:
        if c>=n and n*p<=b:
            prix=n*p
    minprix=min(prix,minprix)
if minprix==100000000:print('stay home')
else:print(minprix)

