for _ in range(int(input())):
    n = int(input())
    s = input()
    f=True 
    for c in range(len(s)):
        for a in range(c+1,len(s)):
            if s[c]==s[a] and (a-c)%2!=0:
                f=False
                break
    print('YES' if f else 'NO')
