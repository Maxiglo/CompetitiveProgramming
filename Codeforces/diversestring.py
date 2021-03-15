alphabet= 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
for i in range(n):
    mot = list(input())
    mot.sort()
    mot = ''.join(mot)
    if mot in alphabet and len(mot)==len(set(mot)):
        print('Yes')
    else:
        print('No')