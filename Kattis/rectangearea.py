a,b,c,d = [float(i) for i in input().split()]
tot = (max(a,c)-min(a,c)) * (max(b,d)-min(b,d))
print(tot)

