import sys
def solve(num):
    c=1
    tot=1
    while(tot%num !=0):
        tot= tot%num
        tot= tot*10+1
        c+=1
    return c

def main():
    for n in sys.stdin:
        print(solve(int(n)))
   
main()