# 2 | 20 22| 200 202 220 222| 2000 2002 2020 2022 2200 2222

n = int(input())
s = bin(n)[2:]
r=""
for c in s:
    if c=='0':
        r+='0'
    else:
        r+='2'
print(r)
