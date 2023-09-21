x,y=map(int, input().split())
grid=[]
for _ in range(x):
    grid.append(input())

def find_words(s):
    w=[]
    temp=''
    for c in s:
        if c!='#':
            temp+=c
        else:
            if len(temp)>1:
                w.append(temp)
            temp=''
    if len(temp)>1:
        w.append(temp)
    return w

words=[]

for row in grid:
    words+=find_words(row)
for col in zip(*grid):
    words+=find_words(''.join(col))
print(sorted(words)[0])