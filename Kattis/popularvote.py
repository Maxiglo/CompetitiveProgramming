for _ in range(int(input())):
    totv=0
    cand=[]
    for _ in range(int(input())):
        v = int(input())
        totv+=v
        cand.append((_,v))
    cand.sort(key=lambda x: x[1], reverse=True)
    if cand[0][1]>totv//2:
        print('majority winner',cand[0][0]+1)
    elif cand[0][1]==cand[1][1]:
        print('no winner')
    else:
        print('minority winner',cand[0][0]+1)
