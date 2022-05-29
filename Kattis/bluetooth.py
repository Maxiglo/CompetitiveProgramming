gauche = ['1+','2+','3+','4+','5+','6+','7+','8+','1-','2-','3-','4-','5-','6-','7-','8-']
droite = ['+1','+2','+3','+4','+5','+6','+7','+8','-1','-2','-3','-4','-5','-6','-7','-8']
g = True 
d = True 
gmu = gml = dmu = dml = 0

for _ in range(int(input())):
    s, x = input().split()
    if s in gauche and x == 'b':
        g = False 
    elif s in droite and x == 'b':
        d = False 
    elif s in droite and x == 'm' and '+' in s:
        dmu+=1
    elif s in gauche and x == 'm' and '+' in s:
        gmu+=1
    elif s in droite and x == 'm' and '-' in s:
        dml+=1
    elif s in gauche and x == 'm' and '-' in s:
        gml+=1

if gml == 8 or gmu == 8:
    g = False 
if dml == 8 or dmu == 8:
    d = False 
if not g and not d:
    print(2)
elif g and not d:
    print(1)
elif d and not g:
    print(0)