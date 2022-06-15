for _ in range(int(input())):
    l = [int(i) for i in input().split()]
    print(sorted(l, reverse=True).index(l[0]))
