m = int(input())

l = [int(i) for i in input().split()]

l.append(l[-1])
last = -1
for c in l:
    if c > last:
        last = c
    else:
        print(last)
        exit()