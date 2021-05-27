import math
n=int(input())
scoremax=0
for i in range(n):
    a,b,c=map(int,input().split())
    score=math.ceil((a+b+c)/3)
    scoremax=max(scoremax,score)

print(scoremax)