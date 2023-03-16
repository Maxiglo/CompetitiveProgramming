for _ in range(int(input())):
    n, s, r = [int(i) for i in input().split()]

    z = n-1

    a = [s-r]

    x = r//z
    reste = r%z
    re = [x for i in range(z)]
    
    i = 0
    while reste>0:
        re[i]+=1
        reste-=1
        i+=1
    a.extend(re)
    print(*a)