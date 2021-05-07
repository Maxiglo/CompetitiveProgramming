    c=0
    for line in fin:
        line=line.split()
        a=int(line[0].split('-')[0])
        b=int(line[0].split('-')[1])
        lettre=line[1][0]
        if a<=line[2].count(lettre)<=b:
            c+=1
    print(c)