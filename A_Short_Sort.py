def solve(s):
    if s in ['abc','acb','bac','cba']:
        print('YES')
    else:
        print('NO')

for _ in range(int(input())):
    s = input()
    solve(s)