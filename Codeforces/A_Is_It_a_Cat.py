for _ in range(int(input())):
    taille = int(input())
    s = input().lower()

    a = '-'
    for c in s:
        if c != a[-1]:
            a += c

    if a == '-meow':
        print("YES")
    else: 
        print("NO")

