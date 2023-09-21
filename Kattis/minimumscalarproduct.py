for _ in range(int(input())):
    n = int(input())
    x1 = [int(i) for i in input().split()]
    x2 = [int(i) for i in input().split()]
    x1.sort()
    x2.sort(reverse=True)
    r=sum([x1[i]*x2[i] for i in range(n)])
    print(f"Case #{_+1}: {r}")