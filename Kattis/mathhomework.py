B, C, D, L = map(int, input().split())

possible = False
for b in range(L//B + 1):
    L1 = L - b * B
    for c in range(L1//C + 1):
        L2 = L - b * B - c * C
        if L2 >= 0 and L2 % D == 0:
            d = L2/D
            if b * B + c * C + d * D == L:
                possible = True
                print(int(b), int(c), int(d))

if not possible:
    print("impossible")