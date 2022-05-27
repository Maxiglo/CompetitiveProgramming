temp = ""
for _ in range(int(input())):
    n = int(input())
    if temp == "":
        temp = n 
    else:
        if n % temp == 0:
            print(n)
            temp = ""