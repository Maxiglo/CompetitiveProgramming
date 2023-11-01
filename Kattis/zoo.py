z = 1
while True:
    n = int(input())
    if n == 0:
        break
    d = {}
    for i in range(n):
        animal = input().split()[-1].lower()
        if animal in d:
            d[animal] += 1
        else:
            d[animal] = 1
    
    print(f'List {z}:')
    # sort by name
    for animal in sorted(d.keys()):
        print(f'{animal} | {d[animal]}')
    z+=1
