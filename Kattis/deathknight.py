n = int(input())
c=0
for i in range(n):
    t= input()
    for j in range(1,len(t)):
        if t[j-1]=='C' and t[j]=='D':
            c+=1
            break
print(n-c)
            


    