n = int(input())
for i in range(n):
    t = input()
    if 'Simon says' in t:
        a= t.replace("Simon says",'')
        print(a)
