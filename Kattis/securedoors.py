s = set()
for _ in range(int(input())):
    x,y = input().split()
    if x=='entry' and y not in s:
        print(f'{y} entered')
        s.add(y)
    elif x=='entry' and y in s:
        print(f'{y} entered (ANOMALY)')
    elif x=='exit' and y in s:
        print(f'{y} exited')
        s.remove(y)
    else:
        print(f'{y} exited (ANOMALY)')