s1=input()
s2=input()
for i in range(len(s1)):
    if s1[i]==s2[i]:
        print('Deletion failed')
        exit()
print('Deletion succeded    ')