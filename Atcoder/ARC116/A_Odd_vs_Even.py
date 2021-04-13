q = int(input())
for i in range(q):
    n= int(input())
    if n%2!=0:
        print('Odd')
    elif n%2==0 and n%4!=0:
        print('Same')
    else:
        print('Even')
