for _ in range(int(input())):
    x = int(input())
    l = [int(i) for i in input().split()]
    x = sum(1 for i in l if i%2==0)
    y = sum(1 for i in l if i%2!=0)
    print(min(x,y))