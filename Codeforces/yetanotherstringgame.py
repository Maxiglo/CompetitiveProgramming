n = int(input())
for i in range(n):
    mot = list(input())
    
    for lettre in range(0,len(mot),2):
        if mot[lettre] !='a':
            mot[lettre]='a'
        elif mot[lettre]=='a':
            mot[lettre]='b'
    for lettre in range(1,len(mot),2):
        
        if mot[lettre]!='z':
            mot[lettre]='z'
        elif mot[lettre]=='z':
            mot[lettre]='y'
    print(''.join(mot))
