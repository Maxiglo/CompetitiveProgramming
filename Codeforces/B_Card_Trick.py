for _ in range(int(input())):
    n = int(input())
    x = [int(i) for i in input().split()]
    k = int(input())
    m = [int(i) for i in input().split()]
    s = sum(m)
    print(x[s%n])