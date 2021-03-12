y,b,r= map(int,input().split())
rep = min(y+2,min(b+1,r))*3-3
print(rep)