n = int(input())
l = [int(i) for i in input().split()]

imp = 0
pair = 0

for i in range(3):
    if l[i] % 2 == 0:
        pair += 1
    else:
        imp +=1

if imp >= 2:
    for i in range(len(l)):
        if l[i]%2 == 0:
            print(i+1)
            break


if pair >= 2:
    for i in range(len(l)):
        if l[i]%2 != 0:
            print(i+1)
            break

