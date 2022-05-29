l = input()
rep = []
for i in range(len(l)-2):
    if (l[i] == ':' and l[i+1] == ')') or (l[i] == ';' and l[i+1] == ')') or (l[i] == ':' and l[i+1] == '-' and l[i+2] == ')') or  (l[i] == ';' and l[i+1] == '-' and l[i+2] == ')'):
        rep.append(i)
if ':)' == l[-2:] or ';)' == l[-2:]:
    rep.append(len(l)-2)
for v in rep:
    print(v)