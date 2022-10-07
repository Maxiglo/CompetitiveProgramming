n, p = map(int, input().split())
results = []
for _ in range(n):
    results.append(int(input()))
results.reverse()

prob = []
score = 0
temp = 0
for r in results:
    if r == 0:
        prob.append(0)
        continue

    if r>temp:
        score += 1
    prob.append(score)
    temp = r
if (score<p or score>p) and temp>0:
    print('ambiguous')
    exit()

for p in reversed(prob):
    print(p)


