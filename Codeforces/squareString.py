n=int(input())
for _ in range(n):
    s=input()
    if len(s)%2!=0:
        print('no')
    else:

        if s[:len(s)//2]==s[len(s)//2:]:
            print('yes')
        else:
            print('no')