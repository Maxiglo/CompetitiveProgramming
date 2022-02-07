lettres = ''
for _ in range(int(input())):
    mot = sorted(input())
    lettres += mot[0]
print(''.join(sorted(lettres)))