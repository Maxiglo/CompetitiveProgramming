for _ in range(int(input())):
    l = [int(i) for i in input().split()]
    tot = 0
    for v in range(1,len(l)-1):
        tot += max((l[v]-l[v-1]*2,0))
    print(tot)
