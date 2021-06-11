n=int(input())
for _ in range(n):
    length=int(input())
    l=[int(i) for i in input().split()]
    minimum=min(l)
    maximum=max(l)
    a=max(l.index(minimum),l.index(maximum))
    b=length-min(l.index(minimum),l.index(maximum))
    x=min(a+1,b)
    print(min(x,length-a+1+min(l.index(minimum),l.index(maximum))))
    