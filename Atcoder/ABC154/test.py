class Solution:
    def solve(self, n):
        n=list(str(n))
        for c in range(len(n)):
            if int(c)<3:
                n[c]='3'
                break
        return(int(''.join(n)))
