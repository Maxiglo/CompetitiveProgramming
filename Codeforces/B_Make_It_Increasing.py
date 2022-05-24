import sys 

input = sys.stdin.readline


def solve(l):
    c = 0
    flag = True 
    for i in range(n-1):
        while l[i+1] >= l[i] and l[i+1]>0:
            l[i+1] //= 2
            c += 1
        if l[i]==l[i+1]:
            return (-1)
    else:return (c)

for _ in range(int(input())):
    n = int(input())
    l = list(reversed([int(i) for i in input().split()]))
    print(solve(l))
