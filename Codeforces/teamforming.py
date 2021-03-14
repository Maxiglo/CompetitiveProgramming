a = int(input())

l= [int(i) for i in input().split()]
l.sort()

somme = 0

for j in range(0,len(l)-1,2):
    somme +=l[j+1]-l[j]
print(somme)