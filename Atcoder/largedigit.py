def somme(s):
    som=int(s[0])+int(s[1])+int(s[2])
    return som
a,b=map(str,input().split())
print(max(somme(a),somme(b)))