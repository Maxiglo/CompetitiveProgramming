n = int(input())

def iscomposite(x):
	c=0
	for i in range(1, x+1):
		if(x % i == 0):
			c += 1
	if c>2:
		return True
	else:
		return False


a,b = n//2,n-n//2

while True:
	if iscomposite(a) and iscomposite(b):
		print(a,b)
		exit()
	a+=1
	b-=1


