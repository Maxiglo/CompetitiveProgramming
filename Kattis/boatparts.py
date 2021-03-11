p,n = map(int,input().split())
s= set()
l=[]
c=0
for i in range(n):
    piece = input()
    s.add(piece)
    if len(l)<p:
        c+=1
        if piece not in l:
            l.append(piece)

if len(s)==p:
    print(c)
else: print('paradox avoided')