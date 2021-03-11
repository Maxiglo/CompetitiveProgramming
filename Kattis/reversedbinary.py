n = int(input())
b = str(bin(n))
c= b[::-1]
c= c[:-2]
print(int(c,2))