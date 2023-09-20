a = input()
b = input()
c = input()

if a == "OOO" or b == "OOO" or c == "OOO":
    print("Jebb")
elif a[0] == "O" and b[0] == "O" and c[0] == "O":
    print("Jebb")
elif a[1] == "O" and b[1] == "O" and c[1] == "O":
    print("Jebb")
elif a[2] == "O" and b[2] == "O" and c[2] == "O":
    print("Jebb")
elif a[0] == "O" and b[1] == "O" and c[2] == "O":
    print("Jebb")
elif a[2] == "O" and b[1] == "O" and c[0] == "O":
    print("Jebb")    
else:
    print("Neibb")