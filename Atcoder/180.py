s=input()
x=s[::-1]
rep=''
for c in x:
    if c!='9' and c!='6':
        rep+=c
    elif c=='9':
        rep+='6'
    else:
        rep+='9'
print(rep)