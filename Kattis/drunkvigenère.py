alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s1= input()
s2=input()
rep=''
for i in range(len(s1)):
    if i%2!=0:
        pos= ((alphabet.index(s1[i])+alphabet.index(s2[i]))%26)
        rep+=alphabet[pos]
    elif i%2==0:
        pos= ((alphabet.index(s1[i])-alphabet.index(s2[i]))%26)
        if pos <0:
            pos = 26-abs(pos)
        rep+=alphabet[pos]

print(rep)