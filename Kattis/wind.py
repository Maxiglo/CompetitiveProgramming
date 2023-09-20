n=int(input())
for _ in range(int(input())):
    name, speed = input().split()
    if int(speed)>=n:
        print(f'{name} opin')
    else:
        print(f'{name} lokud')