for _ in range(int(input())):
    x = int(input())
    for i in range(x,-1,-1):
        if sum(map(int,str(i)))<sum(map(int,str(x))):
            print(i)
            break