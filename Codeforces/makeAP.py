n = int(input())

for _ in range(n):
	a,b,c = map(int,input().split())

	x = 2*b-c # a = b - (c-d)
	u = 2*b-a # c = b + (b-a)
	z = a+c   # b = (a+c)/2
	if (x%a==0 and x>0) or (u%c==0 and u>0) or ((z/2)%b==0 and z/2>0):
		print('yes')
	else:
		print('no')