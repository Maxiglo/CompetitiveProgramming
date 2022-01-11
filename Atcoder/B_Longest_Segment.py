import math

def dist(x,y,a,b):
    return math.sqrt((x-a)**2+(y-b)**2)

l = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    l.append((x,y))


# parcourir tous les elements de la liste et calculer dist en gardant max dist

maxdist = 0

for i in range(len(l)):
    for j in range(i+1,len(l)):
        maxdist=max(maxdist,dist(l[i][0],l[i][1],l[j][0],l[j][1]))
print(maxdist)

    