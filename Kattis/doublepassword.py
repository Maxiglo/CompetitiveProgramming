a = input()
b = input()
t = 0
for c in range(len(a)):
    if a[c] != b[c]:
        t += 1
print(2**t)