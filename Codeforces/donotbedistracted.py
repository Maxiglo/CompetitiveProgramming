n=int(input())
for i in range(n):
    l=int(input())
    s=input()
    vu=[]
    ok=True
    for c in range(len(s)):
        if s[c] in vu and s[c]!=vu[-1] :
            ok=False
        vu.append(s[c])
    print('NO' if not ok else 'YES')
        