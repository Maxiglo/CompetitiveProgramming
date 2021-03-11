a = set(input())
b = input()

mauvais = 0
for i in b:
    if i in a:
        a.remove(i)

        if len(a)==0:
            print('WIN')
            break
    
    else: mauvais +=1
    if mauvais ==10:
        print('LOSE')
        break