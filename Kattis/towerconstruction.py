n = int(input())
l = [int(i) for i in input().split()]
c = 1

for i in range(1,len(l)):
    if l[i]>l[i-1]:
        c+=1

print(c)