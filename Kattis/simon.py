n = int(input())
for i in range(n):
    l = input()
    if l.startswith("simon says"):
        print(' '.join(l.split()[2:]))
    else:
        print('\n')