#code degueu mais il est tard
def solve(s):
    if s[1:].isupper():
        return True
    return False

mot=input()
if len(mot)==1 and mot[0].islower():
    mot=mot.upper()
elif len(mot)==1 and mot[0].isupper():
    mot=mot.lower()
elif solve(mot) and not mot[0].isupper():
    mot= mot.lower().capitalize()
elif solve(mot) and mot[0].isupper():
    mot=mot.lower()
print(mot)

