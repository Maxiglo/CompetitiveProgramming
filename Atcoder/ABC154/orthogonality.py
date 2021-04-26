n=int(input())
l=[int(i) for i in input().split()]
l2=[int(j) for j in input().split()]
somme=0
for i in range(n):
    somme+=l[i]*l2[i]

print('Yes' if somme==0 else 'No')