t = input()
rep =""

for i in range(len(t)-1):
    if t[i]!=t[i+1]:
        rep +=t[i]

rep+=t[-1]
print(rep)
