#implem basique de formule
import math

def pnrom(p,x1,x2,y1,y2):
    return ((abs(x1-x2))**p +(abs(y1-y2))**p)**(1/p)

while True:
    try:
        x1,y1,x2,y2,p= map(float,input().split())
        print(pnrom(p,x1,x2,y1,y2))
    except:
        break