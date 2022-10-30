t = ''
tot = 0
for _ in range(int(input())):
    s = input()
    if s[0] == t:
        tot += 1
    t = s[1]
print(tot+1)
