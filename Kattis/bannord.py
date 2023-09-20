a=input()
s=input().split()
r=[]
def check(word,letters):
    for l in letters:
        if l in word:
            return True 
    return False

for w in s:
    if check(w,a):
        r.append('*'*len(w))
    else:
        r.append(w)
print(*r)