import sys 
n = int(input())
t= list(map(int,sys.stdin.readline().split()))
c=0
for i in t:
    if i<0:
        c+=1
print(c)
