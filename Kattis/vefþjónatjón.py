ta=tb=tc=0
for _ in range(int(input())):
    a,b,c=input().split()
    if a=='J':
        ta+=1
    if b=='J':
        tb+=1
    if c=='J':
        tc+=1
print(min(ta,tb,tc))
