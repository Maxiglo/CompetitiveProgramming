s = input()
a = s.index('(')
b = s.index(')')

if a == len(s) - b - 1:
    print('correct')
else:
    print('fix')