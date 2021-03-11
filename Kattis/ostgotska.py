ligne= input().split()
c=0
for mot in ligne:
    if 'ae' in mot:
        c+=1

if c/len(ligne)>=0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')