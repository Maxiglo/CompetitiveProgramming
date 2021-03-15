t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	d=abs(a-b)
    #ans = diff entre a et v div 5 
	ans=d//5
    #dans le reste de la div par 5 si 3 ou 4 alors 2 opérations à faire sinon 1
	if d%5==4 or d%5==3:
		ans+=2
	elif d%5==2 or d%5==1:
		ans+=1
	print(ans)