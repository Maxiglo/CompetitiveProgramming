def solve(l):
    if len(l) == 1:
        return True
    pairs = -1
    impairs = -1

    for elem in l:
        if elem%2==0:
            if elem < pairs:
                return False
            else:
                pairs = elem
        else:
            if elem < impairs:
                return False
            else:
                impairs = elem
    return True

for _ in range(int(input())):
    x = int(input())
    l = [int(i) for i in input().split()]
    if solve(l):
        print('Yes')
    else:
        print('No')
