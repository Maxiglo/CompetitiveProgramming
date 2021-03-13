mot = input()

n= mot.count('a')
autre = len(mot)-n
c=0
while autre >=n:
    c+=1
    autre-=1

print(len(mot)-c)