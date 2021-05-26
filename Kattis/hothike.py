n=int(input())
l=[int(i) for i in input().split()]

tmin=10000000
for i in range(len(l)-2):
    if max(l[i],l[i+2])<tmin:
        indice=i+1
        tmin=max(l[i],l[i+2])
print(indice,tmin)