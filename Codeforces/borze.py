n = list(input())
rep=''
t =0
while t<len(n):
    if n[t]=='.':
        rep+='0'
        t+=1
    elif n[t]=='-'and n[t+1]=='.':
        rep+='1'
        t+=2
    elif n[t]=='-' and n[t+1]=='-':
        rep+='2'
        t+=2
print(rep)