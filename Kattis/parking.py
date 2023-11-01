a,b,c = map(int, input().split())

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


r = [0 for i in range(101)]

for i in range(x1, y1):
    r[i] += 1
for i in range(x2, y2):
    r[i] += 1
for i in range(x3, y3):
    r[i] += 1

price = 0

for z in r:
    price += z*a if z == 1 else z*b if z == 2 else z*c
print(price)
