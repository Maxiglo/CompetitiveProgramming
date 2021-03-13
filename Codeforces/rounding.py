n =int(input())
while n%10 !=0:
    if int(str(n)[-1])<=5:
        n-=1
    else:
        n+=1
print(n)


