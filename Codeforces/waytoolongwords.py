n = int(input())
for i in range(n):
    mot = input()
    if len(mot)<=10:
        print(mot)
    else:
        print(mot[0]+str(len(mot)-2)+mot[-1])