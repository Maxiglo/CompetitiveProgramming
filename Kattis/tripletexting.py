t = input()
taille = int(len(t)/3)
if t[:taille]==t[taille:2*taille]:
    print(t[:taille])
elif t[:taille]==t[2*taille:3*taille]:
    print(t[:taille])

elif t[taille:2*taille]==t[2*taille:]:
    print(t[2*taille:3*taille])