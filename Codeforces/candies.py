for _ in range(int(input())):
	n = int(input())

	somme = 1
	k=1
	while True:
		if n%somme==0 and k>1:
			print(n//somme)
			break
		somme += 2**k
		k+=1