def solve(x):
    if len(x) == 1:
        return 1

    while True:
        if len(x)==0:
            break
        if x[0] == '0' and x[-1] == '1':
            x = x[1:-1]
        elif x[0] == '1' and x[-1] == '0':
            x = x[1:-1]

        else:
            break 
    return len(x)

for _ in range(int(input())):
    n = int(input())
    s = input()
    rep = solve(s)
    print(rep)
    