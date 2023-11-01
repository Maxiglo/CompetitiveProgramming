s = input()
rep = []
for c in s:
    rep.append(c) 
    if c=='<':
        rep.pop()
        rep.pop()
        
print(''.join(rep))