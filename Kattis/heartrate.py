n = int(input())

for i in range(n):
    b,p = map(float, input().split())
    bpm= (60*b)/p
    print(bpm-(60/p),bpm, bpm+(60/p))
