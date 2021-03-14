t =int(input())

for i in range(t):
    b,p,f= map(int, input().split())
    h,c = map(int,input().split())
    nburger=0
    nchicken=0

    if h>=c:
        while b>1 and f>0:
            if p>0:
                nburger+=1
                b-=2
                p-=1
            else:
                nchicken+=1
                b-=2
                f-=1
    if h<c:
        while b>1 and p>0:
            if f>0:
                nchicken+=1
                b-=2
                f-=1
            else:
                nburger+=1
                b-=2
                p-=1
    print(nburger*h+nchicken*c)
