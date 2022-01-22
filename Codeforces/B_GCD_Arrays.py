for _ in range(int(input())):
    l,r,k = map(int,input().split())
    # nbre pairs -> gcd au moins 2
    # toucher aux nombres impairs les plus petits
    if l == r and l>1:
        print('YES')
        continue
    imp = 0
    if r%2!=0:
        r+=1
    if l%2!=0:
        l-=1
    imp = (r-l)/2

    
    if imp>k:
        print('NO')
    else:
        print('YES')