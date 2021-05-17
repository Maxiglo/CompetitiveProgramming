n=int(input())
l=[]
for i in range(n):
    score,nom=input.split()
    l.append([int(score),nom])
l=sorted(l,key=lambda x:x[0])

print(l[-1][1])