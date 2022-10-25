a,b,c,d,e = map(int, input().split())
note = int(input())

if note>=a: print('A')
elif a>note>=b: print('B')
elif b>note>=c: print('C')
elif c>note>=d: print('D')
elif d>note>=e: print('E')
else: print('F')
