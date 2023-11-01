n = int(input())

s = []
for i in range(n):
    x = [int(i) for i in input().split()] 
    for j,a in enumerate(x):
        if a!=-1:
            s.append((i+1,j+1,a))
s=sorted(s,key=lambda x:(x[0],x[1]))
print(len(s))
for i in s:
    print(*i) 