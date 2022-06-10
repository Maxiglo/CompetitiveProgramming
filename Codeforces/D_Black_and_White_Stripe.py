for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input() 
    temp = best = s[:k].count('W')
    for i in range(k, n): 
        best = min(temp + (s[i] == 'W') - (s[i-k] == 'W'), best)
        temp = temp + (s[i] == 'W') - (s[i-k] == 'W')
    print(best)
