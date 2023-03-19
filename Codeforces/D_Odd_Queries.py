import sys 
input = sys.stdin.readline
def solve():
    for _ in range(int(input())):
        n,q = map(int, input().split()) 
        a = list(map(int, input().split()))
        somme=sum(a)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + a[i]
        for _ in range(q):
            l,r,k = map(int, input().split())
            if (somme-prefix_sum[r]+prefix_sum[l-1]+(r-l+1)*k) % 2 == 0:
                print('NO')
            else:
                print('YES')
solve()