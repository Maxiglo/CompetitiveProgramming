n, m = map(int, input().split())
s1 = input().split()
s2 = set(input().split())
## x i s = O(1) si c'est un set alors que O(n) si c'est une liste !
for c in s1:
    if c not in s2:
        print('No')
    else:
        print('Yes')