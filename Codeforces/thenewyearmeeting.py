num = [int(i) for i in input().split()]

snum= sorted(num)
print(snum[-1]-snum[0])