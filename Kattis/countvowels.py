s = input().lower()
v = 'aeiou'
print(sum(1 for c in s if c in v))