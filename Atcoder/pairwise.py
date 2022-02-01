a=int(input())
l=[int(i) for i in input().split()]
if len(set(l)) ==a:
    print('YES')
else:
    print('NO')

