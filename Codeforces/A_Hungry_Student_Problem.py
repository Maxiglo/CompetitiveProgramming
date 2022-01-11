# équation -> 3x+7y = n

def solve(x):
    if x%3==0 or x%7==0 or x%10==0:
        return 'YES'
    
    for i in range(101):
        for j in range(101):
            if 3*i+7*j==x:
                return 'YES'
    return 'NO'


for _ in range(int(input())):
    n = int(input())
    print(solve(n))


