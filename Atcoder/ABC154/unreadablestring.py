def solve(s):
    ok=True
    for i in range(1,len(s),2):
        if s[i].islower():
            ok=False
    for j in range(0,len(s),2):
        if s[j].isupper():
            ok=False
    return ok
s=input()
print('Yes' if solve(s) else ('No'))