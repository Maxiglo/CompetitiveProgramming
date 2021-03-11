'''a,b = map(int,input().split())
notes = input().split()
c=0

for i in range(a):
    if int(notes[i])>=int(notes[b-1]) and int(notes[i])>0:
        c+=1
print(c)
'''
a,b = map(int,input().split())
 
notes = [int(i) for i in input().split()]
c=0
for note in notes:
    if note>=notes[b-1] and note>0:
        c+=1
print(c)