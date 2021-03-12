n = int(input())
sommex=0
sommey=0
sommez=0
for i in range(n):
    x,y,z= map(int,input().split())
    sommex+=x
    sommey+=y
    sommez+=z
if sommex==sommez==sommey==0:
    print('YES')
else:
    print('NO')