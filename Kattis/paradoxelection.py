n = int(input())
l = sorted([int(i) for i in input().split()], reverse = True)

tot = sum(l[i] for i in range(len(l)//2)) + sum(l[i]//2 for i in range(len(l)//2,len(l),1))

print(tot)