a,b = map(int,input().split())
trouve = False
while a<=b:
    if len(set(list(str(a))))==len(str(a)):
        trouve = True
        print(a)
        break
    a+=1
  
if not trouve:
    print(-1)