n = input()

if n ==n[::-1]:
    print('Yes')


else:
    l = list(n)
    for i in range(len(l)-1,0,-1):
        if l[i] =='0':
            l.pop()
        else:
            break
    
    if ''.join(l) ==''.join(l)[::-1]:
        print('Yes')
    else:
        print('No')
