n = int(input())
l = [int(i) for i in input().split()]

l = sorted(l, reverse= True)

tot = sum(l)
x = 0
i = 0
# x = total qu'on a 
# tant que x <= reste alors on ajoute
while x <= tot - x:
    x += l[i]
    i += 1
print(i) 
