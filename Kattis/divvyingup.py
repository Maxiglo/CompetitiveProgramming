n = int(input())
if sum([int(i) for i in input().split()]) % 3 == 0:
    print('yes')
else:
    print('no')