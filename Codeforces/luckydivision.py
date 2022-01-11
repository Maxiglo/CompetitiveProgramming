def islucky(x):
    x = list(str(x))
    for c in x:
        if c!='4' and c!='7':
            return False
    return True


n = int(input())
div = [int(i) for i in range(1,n+1) if (n%i==0 and  islucky(i))]


if len(div)>0:
    print('YES')
else:
    print('NO')