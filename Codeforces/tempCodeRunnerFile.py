import sys
input=sys.stdin.readline
from itertools import combinations

n=int(input())

def main():
    for _ in range(n):
        c=0
        n,l,r=map(int,input().split())
        a=[int(i) for i in input().split()]
        for subset in combinations(a, 2):
            if l<=sum(subset)<=r:
                c+=1    
        print(c)
main()