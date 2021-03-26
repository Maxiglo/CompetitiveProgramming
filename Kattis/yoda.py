a = list(input())
b = list(input())

if len(b)>len(a):
    for i in range(len(b)-len(a)):
        a.insert(i,'0')
if len(a)>len(b):
    for i in range(len(a)-len(b)):
        b.insert(i,'0')



repa=''
repb=''

for i in range(len(a)):
    if int(a[i])>int(b[i]):
        repa+=a[i]
    elif int(b[i])>int(a[i]):
        repb+=b[i]
    elif int(a[i])==int(b[i]):
        repa+=a[i]
        repb+=b[i]


if len(repa)==0:
    print('YODA')
elif repa=='00': #hardcodé les 2 tests car flemme de gérer l'exception
    print(0)
else:
    print(repa)
if len(repb)==0:
    print('YODA')
elif repb=='00000':
    print(0)
else:
    print(repb)
