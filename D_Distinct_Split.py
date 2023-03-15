for _ in range(int(input())):
    n = int(input())
    s = input()

    rep = 0

    a = set()
    ta = []

    for c in s:
        a.add(c)
        ta.append(len(a))
    b = set()
    for i in range(n-1, -1, -1):
        rep = max(rep, ta[i] + len(set(b)))
        b.add(s[i])
    print(rep)
        





 
