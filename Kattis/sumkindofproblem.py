k = int(input())

for j in range(k):
    n,m = map(int,input().split())
    s1=0
    s2=0
    s3=0
    for i in range(1,m+1):
        s1+=i
    for i in range((2*m)+1):
        if i%2==0:
            s3+=i
        else:
            s2+=i
    print(j+1,s1,s2,s3)