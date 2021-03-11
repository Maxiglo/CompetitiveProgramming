import sys
n = input()
a = list(map(int,sys.stdin.readline().split()))
somme = 0
for i in a:
    if i<0:
        somme+=i
print(abs(somme))