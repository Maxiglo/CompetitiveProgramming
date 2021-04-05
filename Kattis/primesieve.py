#https://codegolf.stackexchange.com/questions/74269/calculate-the-number-of-primes-up-to-n
#problème qui ne passe pas avec eratosthène, pas la bonne méthode ici mais passe parfaitement avec cette méthode
import sys
input= sys.stdin.readline
def Phi(m, b):
    if not b:
        return m
    if not m:
        return 0
    if m >= 800:
        return Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
    t = b * 800 + m
    if not Phi_memo[t]:
        Phi_memo[t] =  Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
    return Phi_memo[t]

x,n = map(int,input().split())

if x < 6:
    print ([0, 0, 1, 2, 2, 3][x])
    exit()

root2 = int(x ** (1./2))
root3 = int(x ** (1./3))
top = x // root3 + 1
sieve = [0, 0] + [1] * (top - 2)
pi = [0, 0]
primes = []
t = 0

for i in range(2, top):
    if sieve[i] == 1:
        t += 1
        primes.append(i)
        sieve[i::i] = [0] * len(sieve[i::i])
    pi.append(t)

a, b = pi[root3 + 1], pi[root2 + 1]
Phi_memo = [0] * ((a + 1) * 800)

print (Phi(x, a) + a - 1 - sum(pi[x // p] - pi[p] + 1 for p in primes[a:b]))
def isPrime_v3(n):
    if n%2==0 or n%3==0:
        False
    else:  
        k = 1
        while(6*k-1)*(6*k-1)<=n:
            if(n%(6*k-1))==0 or n%(6*k+1)==0:
                return False
            k+=1
        return True
def main():
    for _ in range(n):
        num = int(input())
        if num==1:
            print(0)
        elif num==2:
            print(1)
        elif num==3:
            print(1)
        elif isPrime_v3(num):
            print(1)
        else:
            print(0)
main()