x = int(input())

ls = [i for i in input().split()]
rep=[]
for j in range(len(ls)-1,-1,-1):
    if ls[j] not in rep:
        rep.append(ls[j])
print(len(rep))
print(' '.join(rep[::-1]))