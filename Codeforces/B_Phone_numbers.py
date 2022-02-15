n=input()
s=input()
for i in range(int(n)):
    print(s[i],end='')
    if i%2==1 and int(n)-2!=i and int(n)-1!=i:print('-', end='')