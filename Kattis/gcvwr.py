a,b,c = map(int, input().split())
l = sum([int(i) for i in input().split()])

print(int(0.9*(a-b)-l))