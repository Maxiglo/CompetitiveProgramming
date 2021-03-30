inf = 1
sup = 1000
mid = 500
print(mid)

while True:
    try:
        rep = input()
        if rep=="correct":
            break
        elif rep =="lower":
            sup = mid-1
        elif rep=="higher":
            inf = mid +1
        mid = (inf + sup)//2
        print(mid)
    except EOFError:
        break