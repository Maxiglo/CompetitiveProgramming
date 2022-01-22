# on sait que 1 2 3 4 5 = (5*6)/2
def mex(arr):
    arr = set(arr)
    mex = 0
    while mex in arr:
        mex += 1
    return mex 
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    i = 0
    s=0
    rep = []
    temp = 0
    for x in range(len(a)):
        m = mex(a[s:i])
        if m <= temp and a[x] in a[s:i]:
            s = i
            rep.append(m)

        

        temp = m
        i+=1
    rep.append(mex(a[s:]))
    if rep[0]==0:
        print(len(rep)-1)
        print(*rep[1:])
    else:
        print(len(rep))
        print(*rep)