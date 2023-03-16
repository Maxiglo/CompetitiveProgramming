for _ in range(int(input())):
    a = int(input())
    s = input() 
    m = 0 
    for c in s:
        m = max(m, ord(c)-96)
    print(m)