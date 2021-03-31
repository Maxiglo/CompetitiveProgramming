#il faut utiliser sys.stdin pour lire les entrées car bcp plus rapide que input et ici ENORME entrée
import sys
while True:
    n,m = [int(i) for i in sys.stdin.readline().split()]
    if n==m==0:
        break
    
    s1= set(int(sys.stdin.readline()) for _ in range(n))
    s2= set(int(sys.stdin.readline()) for _ in range(m))
    print(len(s1&s2))
