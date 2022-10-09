corner, edge, center = map(int, input().split())

if corner != 4 or edge %2 != 0: 
    print('Impossible')
    exit()

# aire totale
aire = corner + edge + center
# somme h+w
hw = edge//2 + corner
i = 1 
while i*i<=aire and i+i<=hw:
    if (hw-i)*i == aire:
        print(i, hw-i)
        exit()
    i+=1
print('impossible')