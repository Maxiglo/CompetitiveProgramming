import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    f = False 
    x = input()
    arr = sorted([int(i) for i in input().split()])
    for x in range(len(arr)-2):
        if arr[x] == arr[x+1] == arr[x+2]:
            print(arr[x])
            f = True 
            break 
    if not f:
        print(-1)
    