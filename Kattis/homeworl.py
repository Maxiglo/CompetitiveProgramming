s = input().split(';')

tot = 0
for val in s:
    if '-' in val:
        x,y = val.split('-')
        tot+=int(y)-int(x)+1 
    else:
        tot+=1
print(tot)