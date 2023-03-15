for _ in range(int(input())):
    n = int(input())
    s = input() 

    x = y = 0 

    f = False 
    for c in s:
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1

        if x==1 and y==1:
            f = True 
            break
    print('NO' if not f else 'YES')