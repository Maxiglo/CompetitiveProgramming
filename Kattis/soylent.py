import math
n = int(input())

for i in range(n):
    c = int(input())
    a = c/400
    if a.is_integer():
        print(int(a))
    else: print(math.ceil(a))