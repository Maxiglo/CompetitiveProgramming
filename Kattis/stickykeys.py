s=input()
rep=s[0]
for i in range(len(s)):
    if s[i] != rep[-1]:
        rep+=s[i]
print(rep)