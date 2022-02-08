def div(n):
    return len([i for i in range(1,n+1) if n%i == 0])

def solve(a,b):
    tot = 0
    for i in range(a,b+1):
        if div(i)%2 != 0:
            tot += 1
    return tot 
a,b = map(int,input().split())
print(solve(a,b))
