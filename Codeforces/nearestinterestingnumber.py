n = int(input())

while True:
    if sum(map(int,list(str(n))))%4==0:
        rep= n
        break
    else:
        n+=1
print(rep)