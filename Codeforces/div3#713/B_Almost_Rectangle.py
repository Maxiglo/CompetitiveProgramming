n = int(input())

def solve(l):
    coord=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j]=='*':
                coord.append((i,j))
    return coord



for i in range(n):
    a = int(input())
    l=[]
    for i in range(a):
        l.append(list(input()))
    c= solve(l)
    x=c[0][0]
    y=c[0][1]
    x2=c[1][0]
    y2=c[1][1]
    if x!=x2 and y!=y2:
        l[x][y2]='*'
        l[x2][y]='*'
    elif x==x2:
        if x==a-1:
            l[x-1][y2]='*'
            l[x2-1][y]='*'
        else:
            l[x+1][y2]='*'
            l[x2+1][y]="*"
    elif y==y2:
        if y==a-1:
            l[x][y2-1]="*"
            l[x2][y-1]='*'
        else:
            l[x][y2+1]="*"
            l[x2][y+1]="*"
    for k in range(len(l)):
        print(''.join(l[k]))