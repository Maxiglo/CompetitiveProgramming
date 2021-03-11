texte = input()

white = texte.count("_")
print(white/len(texte))
c=0
d=0
k=0
for i in texte:
    if i.islower():
        c+=1
    if i.isupper():
        d+=1


print(c/len(texte))
print(d/len(texte))
print((len(texte)-white-c-d)/len(texte))
