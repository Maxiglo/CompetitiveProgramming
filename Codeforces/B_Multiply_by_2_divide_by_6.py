def solve(x):
    c = 0
    z = x

    while True:
        if x==1:
            return c
        if c>=z:
            return -1
        else:
            if x%6==0:
                x/=6
            elif x%3==0:
                x*=2
            else:
                return -1
        c+=1


for _ in range(int(input())):
    n = int(input())
    print(solve(n))