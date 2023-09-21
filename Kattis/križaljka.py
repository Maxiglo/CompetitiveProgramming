a,b=input().split()

for i in a:
    if i in b:
        idxb = b.index(i)
        idxa = a.index(i)
        break 

s = '.'*len(a)
for i in range(len(b)):
    if i==idxb:
        print(a)
    else:
        print(s[:idxa]+b[i]+s[idxa+1:])