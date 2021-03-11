import sys 
n = int(input())
nombre = list(map(int,sys.stdin.readline().split()))

som= 0
npositif=0
for i in nombre:
    if i>=0:
        npositif +=1
        som += i
        ans = som/npositif
print(ans)
    