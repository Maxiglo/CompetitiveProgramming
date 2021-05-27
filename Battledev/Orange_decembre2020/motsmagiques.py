n=int(input())
voy='aeiouy'
mots=set()
for _ in range(n):
    s=input().lower()
    magique=True
    if len(s)<5 or len(s)>7:
        magique=False
    if ord(s[0])!=ord(s[1])-1:
        magique=False
    if s[-1] not in voy:
        magique=False
    if magique:
        mots.add(s)
print(len(mots))