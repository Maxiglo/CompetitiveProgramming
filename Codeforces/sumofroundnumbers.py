for _ in range(int(input())):
    nombre = input()
    n = len(nombre)-1
    ans=[]
    for i in nombre:
        if i!='0':
            ans.append(int(i)*(10**n))
        n-=1
    print(len(ans))
    print(*ans)