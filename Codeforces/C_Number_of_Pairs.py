from bisect import bisect_left, bisect_right
 
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = sorted([int(i) for i in input().split()])
    ans = 0
    for i in range(n):
        # il, ir permet de trouver l'intervalle dans lequel on peut add a[i] à n'importe quel nombre de l'intervalle pour être entre l et r
        il = bisect_left(a, l - a[i])
        ir = bisect_right(a, r - a[i])
        ir = min(ir, i)
        ans += max(0, ir - il)
    print(ans)