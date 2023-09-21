import sys

for line in sys.stdin:
    rep = ''
    s = line.strip() 
    temp = s[0]
    for i in s[1:]:
        if i == temp[-1]:
            temp += i
        else:
            rep += str(len(temp)) + temp[0]
            temp = i
    rep += str(len(temp)) + temp[0]
    print(rep)
