        if n[i] =='0':
            n.replace('0','')
        else:
            break
    print(n)
    if n ==n[::-1]:
        print('Yes')
    else:
        print('No')
