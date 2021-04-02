#ne fonctionne pas, il faudrait stocker les valeurs dans une liste pour pas recalculer à chaque fois mais flemme il est tard
import sys,math 

def solve(n):
    somme = 0
    for i in range(len(str(n)),n+1):
        somme+=math.log(i,10)
    return(math.floor(somme)+1)
    

def main():
    for line in sys.stdin:
        print(solve(int(line.strip())))
if __name__=='__main__':
    main()