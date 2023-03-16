for _ in range(int(input())):
    s = input()
    rep = 0
    pi = '314159265358979323846264338327950288419716939937510582097494459230781640628620899'
    for i,c in enumerate(s):
        if pi[i] == c:
            rep+=1
        else:
            break
    print(rep) 
         