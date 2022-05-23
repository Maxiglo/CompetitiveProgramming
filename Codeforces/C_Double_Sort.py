def sort(a, b):
    x = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
                x.append([j+1,i+1])

    for i in range(len(a)):
        for j in range(i, len(a)):
            if b[j] < b[i]:
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
                x.append([j+1,i+1])
    if b != sorted(b) or a!= sorted(a):
        return -1 
    else:
        return x           

for _ in range(int(input())):
    k = int(input())
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    z = sort(arr1, arr2)
    if z == -1:
        print(-1)
    elif len(z)==0:
        print(0)
    else:
        print(len(z))
        for x in z:
            print(*x)