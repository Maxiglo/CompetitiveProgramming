n = input()

c= 1
maximum=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
        if c>maximum:
            maximum=c
    else:
        c=1
if maximum>=7:
    print('YES')
else:
    print('NO')