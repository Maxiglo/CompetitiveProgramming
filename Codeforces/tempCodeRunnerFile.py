s = input()


if ('h' and 'e' and 'l' and 'l' and 'o' not in s) or len(s)<5:
    print('NO')
    exit()

pos= s.index('h')
s= s[pos:]
if 'e' not in s:
    print('NO')
    exit()
else:
    pos=s.index('e')

s= s[pos:]
if 'l' not in s:
    print('NO')
    exit()
else:
    pos=s.index('l')+1
s = s[pos:]

if 'l' not in s:
    print('NO')
    exit()
else:
    pos=s.index('l')
s = s[pos:]

if 'o' not in s:
    print('NO')
else:
    print('YES')
