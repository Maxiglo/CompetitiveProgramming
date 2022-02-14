for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    x=1
    y=z=-1
    for i in range(len(l)):
        if l[i]==x:
            x+=1
            continue
        else:
            y,z=i,l.index(x)
            break
    if y==z==-1:print(*l)
    else:
        l[y:z+1]=l[y:z+1][::-1]
        print(*l)