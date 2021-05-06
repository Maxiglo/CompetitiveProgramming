with open('jour1entrée.txt','r') as fin:
    l=[]
    for line in fin:
        l.append(line.strip())

#part one
for i in l:
    for j in l:
        if int(i)+int(j)==2020:
            print(int(i)*int(j))
#part two
for i in l:
    for j in l:
        for k in l:
            if int(i) +int(k) +int(j)==2020:
                print(int(i)*int(j)*int(k))
                break