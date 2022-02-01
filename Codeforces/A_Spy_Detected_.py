n = int(input())
for i in range(n):
    a = int(input())
    l=[int(j) for j in input().split()]
    for num in l:
        if l.count(num)==1:
            print(l.index(num)+1)
