n = int(input())
d= {}
for i in range(n):
    a,b = input().split()
    if a.isdigit():
        a = int(a)/2
        d[b]=int(a)
    else: 
        d[a]= int(b)

dicsorted= dict(sorted(d.items(), key= lambda x:x[1]))

for clef,valeur in dicsorted.items():
    print(clef)  
