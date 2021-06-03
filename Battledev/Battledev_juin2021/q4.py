import sys

taille=int(input())

nDivisions = 0

string = input()
if taille%2==1:
    print(0)
    exit()
for i in range(0,taille//2):
    for j in range(i,taille//2+i):
        list1=string[i:taille//2+i]
        list2=string[taille//2+i:taille]+string[0:i]

        if sorted(list1)==sorted(list2):
            nDivisions+=2
print(nDivisions)