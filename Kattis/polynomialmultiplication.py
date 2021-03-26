#problème sympa
t = int(input())
#fct qui calcule la multipliaction de 2 polynômes
def polynom(s1,s2):
    res = [0]*(len(s1)+len(s2)-1)
    for o1,i1 in enumerate(s1):
        for o2,i2 in enumerate(s2):
            res[o1+o2] += i1*i2
    return res

for i in range(t):
    n= int(input()) #degree
    s1 = [int(i) for i in input().split()] #coef
    n2= int(input())
    s2=[int(j) for j in input().split()]
    print(n+n2)
    print(*polynom(s1,s2))

