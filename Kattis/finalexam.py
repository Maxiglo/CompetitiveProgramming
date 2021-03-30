#nul
n = int(input())
l=''
for i in range(n):
    l+=input()
score = 0
for lettre in range(len(l)-1):
    if l[lettre+1]==l[lettre]:
        score+=1
print(score)