#utiliser eval permet d'évaluer une expression directement dans le code
#problème sympa, permet d'utiliser eval(string)
a,b,c = [int(i) for i in input().split()]

operateurs= ['+','-','*','/']

for op in operateurs:
    string = str(a) + op + str(b)
    string2= str(b) + op +str(c)
    if eval(string)==c:
        print(f"{a}{op}{b}={c}")
        

    elif eval(string2)==a:
        print(f"{a}={b}{op}{c}")
        break