with open('jour2entrée.txt','r') as fin:
    #part one
    c=0
    valid =0
    for line in fin:
        line=line.split()
        a=int(line[0].split('-')[0])
        b=int(line[0].split('-')[1])
        lettre=line[1][0]
        if a<=line[2].count(lettre)<=b:
            c+=1
    #part two
        if (line[2][a-1]==lettre and line[2][b-1]!=lettre) or ((line[2][a-1]!=lettre and line[2][b-1]==lettre)):
            valid+=1    
    print(c)
    print(valid)
