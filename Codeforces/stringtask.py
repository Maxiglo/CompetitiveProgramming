def solve():
    s = list(input().lower())
    voy= 'aeiouy'
    rep=[]
    for i in range(len(s)):
        if s[i] not in voy:
            rep.append(s[i])

    for i in range(len(rep)*2):
        if i%2==0:
            rep.insert(i,'.')
    print(''.join(rep))
solve()