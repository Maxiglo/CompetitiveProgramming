a = input()
b = a.replace("+"," ").split()
b =sorted(b)
print('+'.join(b))