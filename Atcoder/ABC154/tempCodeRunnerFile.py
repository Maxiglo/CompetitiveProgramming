s=input()
op=['+','-']

for op1 in op:
    for op2 in op:
        for op3 in op:
            if eval(s[0]+op1+s[1]+op2+s[2]+op3+s[3])==7:
                print(s[0]+op1+s[1]+op2+s[2]+op3+s[3]+'=7')
                break

