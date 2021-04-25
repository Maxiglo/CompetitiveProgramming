n,k=map(int,input().split())
if k<=(n//2)+1:
    l=[int(i) for i in range(1,n+1,2)]
    print(l[k-1])
else:
    l2=[int(j) for j in range(2,n+1,2)]
    print(l2[k-((n//2)+1)-1])
  