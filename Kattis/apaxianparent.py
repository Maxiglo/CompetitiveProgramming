a,b= input().split()
voyelle = 'aiou'
if a[-1]=='e':
    print(a+'x'+b)
elif a[-1] in voyelle:
    print(a[:-1]+'ex'+b)

elif a[-2:]=='ex':
    print(a+b)

else: 
    print(a+'ex'+b)