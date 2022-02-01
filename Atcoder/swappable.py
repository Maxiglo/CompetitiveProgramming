import itertools
n=int(input())
l=[int(i) for i in input().split()]
s= sum(1 for subset in itertools.combinations(l, 2) if len(set(subset))==2)
print(s)