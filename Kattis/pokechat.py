enc = input()
s = input()

rep=""
for i in range(0,len(s),3):
    idx = int(s[i:i+3])-1
    rep+=enc[idx]
print(rep)