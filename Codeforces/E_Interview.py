import sys 

for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    # borne inférieure
    a=0
    # borne supérieure
    b=n-1 
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+l[i]

    while a<b:
        mid = (a+b)//2
        
        print('?',mid-a+1,*range(a+1,mid+2), flush=True)

        rep = int(input())
        if rep == s[mid+1]-s[a]:
            a = mid+1
        else:
            b = mid

    print('!',a+1,flush=True)