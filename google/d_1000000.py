for _ in range(int(input())):
    x = int(input())
    l = sorted([int(i) for i in input().split()])
    goal = 1 
    tot = 0
    for j in range(len(l)):
        if l[j] >= goal:
            tot += 1
            goal += 1
        else:
            continue
        
    print(f'Case #{_+1}: {tot}')