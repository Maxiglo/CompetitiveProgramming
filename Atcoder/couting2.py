n,q = map(int,input().split())

l = [int(i) for i in input().split()]

for _ in range(q):
    x = int(input())

    print(len(list(filter(lambda z:z >= x,l))))
    
