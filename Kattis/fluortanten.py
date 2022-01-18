n = int(input())
l = [int(i) for i in input().split()]
l.remove(0)

def score(l):
    score = 0
    for i in range(len(l)):
        score += (i+1)*l[i]
    return score 

bestscore = -10**10
for i in range(len(l)+1):
    l.insert(i, 0)
    bestscore = max(bestscore,score(l))
    l.remove(0)
print(bestscore)