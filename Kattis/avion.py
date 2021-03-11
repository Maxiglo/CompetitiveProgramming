a= input()
b = input()
c = input()
d = input()
e = input()

l=[]

if 'FBI' in a:
    l.append(1)
if 'FBI' in b:
    l.append(2)
if 'FBI' in c:
    l.append(3)
if 'FBI' in d:
    l.append(4)
if 'FBI' in e:
    l.append(5)
if len(l)==0:
    print("HE GOT AWAY!")
else:
    for i in l:
        print(i, end=" ")