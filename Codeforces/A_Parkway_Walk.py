for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    print(max(sum(a)-m,0))