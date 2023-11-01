base = 'codeforces'
for _ in range(int(input())):
    s = input()
    tot = 0
    for i,c in enumerate(s):
        if base[i]!=c:
            tot+=1
    print(tot)
