t=l=0
for _ in range(int(input())):
    s = input()
    if s[0]=='0':
        t+=1
    if s[1]=='0':
        t+=1
    if s[2]=='0':
        l+=1
    if s[3]=='0':
        l+=1
r=min(t//2,l//2)
print(r,t-2*r,l-2*r)