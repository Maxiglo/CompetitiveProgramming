def solve(l):
    if len(l) == 1:
        return True
    p = [int(i) for i in l if i%2==0]
    imp = [int(i) for i in l if i%2 != 0]

    if p == sorted(p) and imp == sorted(imp):
        return True 
    return False

for _ in range(int(input())):
    x = int(input())
    l = [int(i) for i in input().split()]
    if solve(l):
        print('Yes')
    else:
        print('No')
