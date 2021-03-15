n = int(input())
sommes=[]
for i in range(n):
    l = map(int,input().split())
    sommes.append(sum(l))

c =0
for j in range(1,len(sommes)):
    if sommes[j]<=sommes[0]:
        c+=1
print(n-c)
