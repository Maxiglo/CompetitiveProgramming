a = int(input())
l = [int(i) for i in input().split()]

biceps=0
back=0
chest=0
for i in range(0,len(l),3):
    chest+=l[i]
for j in range(1,len(l),3):
    biceps+=l[j]
for k in range(2,len(l),3):
    back+=l[k]

rep = max(chest,biceps,back)
if rep==chest:
    print('chest')
elif rep==biceps:
    print('biceps')
else:
    print('back')