n = int(input()) + 1 

while True:
    if len(str(n)) == len(set(str(n))):
        print(n)
        break 
    else:
        n += 1