n = int(input())

for i in range(n):
    a = int(input())
    s = set()
    for i in range(a):
        t = input()
        s.add(t)

    print(len(s))