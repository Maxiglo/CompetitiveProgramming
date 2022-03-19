s= input()
tot = 0
coef = [4,3,2,7,6,5,0,4,3,2,1]

for i in range(len(s)):
    if s[i].isalnum():
        tot += int(s[i]) * coef[i]
print(1 if tot % 11 == 0 else 0)