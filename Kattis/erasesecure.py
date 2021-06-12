n=int(input())
s1=input()
s2=input()
if n%2!=0:
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            print('Deletion failed')
            exit()
    print('Deletion succeeded')
else:
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            print('Deletion failed')
            exit()
    print('Deletion succeeded')