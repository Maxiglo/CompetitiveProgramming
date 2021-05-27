n=int(input())
c=0
for _ in range(n):
    s=input()
    if s[-5:].isdigit():
        c+=1
print(c)