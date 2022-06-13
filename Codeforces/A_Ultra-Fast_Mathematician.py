a = input()
b = input()
rep = [int(x)^int(y) for x,y in zip(a,b)]
print(''.join(map(str,rep)))