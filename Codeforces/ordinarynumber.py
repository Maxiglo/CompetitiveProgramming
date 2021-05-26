import math
def count_same_digit(L, R):
    tmp = 0
    ans = 0
    n = int(math.log10(R) + 1)
    for i in range(0, n):
        tmp = tmp * 10 + 1
 
 
        for j in range(1, 10):
 
            if (L <= (tmp * j) and (tmp * j) <= R):
                ans += 1
 
    return ans
 
 
def main():
 
    t=int(input())
    for x in range(t):
        c=int(input())
        print(count_same_digit(1, c))
main()