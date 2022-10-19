l = [int(input()) for _ in range(9)]
tot = sum(l)

for a in range(9):
    for b in range(9):
        if tot-l[a]-l[b]==100 and a!=b:
            x,y = a,b 
            break 
for i in range(len(l)):
    if i!=x and i!=y:
        print(l[i]) 