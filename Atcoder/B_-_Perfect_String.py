s = input()

up = False
low = False 
diff = True 

for i,c in enumerate(s):
    if c.isupper(): up = True 
    if c.islower(): low = True 
    for k in range(i+1, len(s)):
        if s[k] == c:
            diff = False 
print('Yes' if up and low and diff else 'No')
