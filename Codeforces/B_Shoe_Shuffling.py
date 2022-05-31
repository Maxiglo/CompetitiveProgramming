from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().split()]
    flag = False 
    pos = defaultdict(list)
    for i,c in enumerate(s):
        pos[c].append(i+1)

    for k in pos.values():
        if len(k)==1:
            flag = True 


    if flag: print('-1')
    else:
        for k,v in pos.items():
            x = v.pop(0)
            v.append(x)
            print(*v, end = ' ')
        print('')
        


