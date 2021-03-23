n = int(input())

for i in range(n):
    l = int(input())
    s = input()
    c=0
    for j in range(len(s)-1,-1,-1):
        if s[j]==')':
           c+=1
        else:
            break
    
    if (l-c>=c):
        print('No')
    else:
        print('Yes') 