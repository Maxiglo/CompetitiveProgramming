(x,y), r = [int(i) for i in input().split()], int(input())
[print(x+dx,y+dy) for dx,dy in [(r,r),(r,-r),(-r,-r),(-r,r)]]
