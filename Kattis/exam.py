a= int(input())

moi = input()
toi = input()
c=0
for i in range(len(moi)):
    if moi[i]==toi[i]:
        c+=1
if c >= a:
    print(a + len(moi) - c)
else:
    print(c + (len(moi) - a))