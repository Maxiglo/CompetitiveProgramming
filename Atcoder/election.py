d = {} 

for _ in range(int(input())):
    x = input()
    if x not in d:
        d[x] = 1
    else:
        d[x]+=1

d = dict(sorted(d.items(),key= lambda x:x[1],reverse = True))
print(list(d)[0])
