n,k=map(int,input().split())
somme=0
for i in range(k):
    somme+=int(input())
m=(n-k)*3+somme
mn=(n-k)*(-3)+somme
print(mn/n,m/n)