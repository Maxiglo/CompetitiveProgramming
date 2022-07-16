a,b = map(int, input().split())
x = [int(i) for i in input().split()]

seuil = x[b-1]

print(sum(1 for i in x if i >= seuil and i > 0))