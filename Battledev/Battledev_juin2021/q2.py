n=int(input())
l=[]
for i in range(n):
    l.append(input())

for mot in l:
    if l.count(mot)==2:
        print(mot)
        break