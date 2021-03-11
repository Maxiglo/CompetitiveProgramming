l = (int(i) for i in input().split())
l = sorted(l)
a= l[3]-l[0]-l[1]
b= l[3]-l[1]-l[2]
c=  l[3]-l[0]-l[2]
print(abs(a),abs(b),abs(c))