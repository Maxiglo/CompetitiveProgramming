n = int(input())
s= input()

scoreA=0
scoreB=0

if s[-1]=='A':
    scoreA= 2
    if len(s)>100:
        scoreB=1
    else:
        scoreB=0
else:
    scoreB=2
    if len(s)>100:
        scoreA=1
    else:
        scoreA=0

print(scoreA,scoreB)




